import asyncio
import json
import logging
from typing import Dict, List
from datetime import datetime
from astrbot.api import logger

try:
    from aiohttp import web
    AIOHTTP_AVAILABLE = True
except ImportError:
    AIOHTTP_AVAILABLE = False
    logger.warning("aiohttp模块未安装，HTTP服务器将不可用")


class TokenHttpServer:
    """HTTP服务器：用于接收自动上报的ChatGPT AccessToken（解决CSP问题）"""
    
    def __init__(self, port: int = 5103):
        self.port = port
        self.tokens: Dict[str, dict] = {}  # token -> token_data
        self.is_running = False
        self.app = None
        self.runner = None
        self.site = None
        
    async def start(self):
        """启动HTTP服务器"""
        if not AIOHTTP_AVAILABLE:
            logger.error("无法启动HTTP服务器：aiohttp模块未安装")
            return False
            
        try:
            # 启动HTTP服务器
            await self.start_http_server()
            
            self.is_running = True
            logger.info(f"✅ HTTP服务器已启动，监听端口: {self.port}")
            logger.info(f"🌐 Token上报端点: http://localhost:{self.port}/api/token")
            logger.info(f"🏥 健康检查: http://localhost:{self.port}/health")
            logger.info(f"📊 Token列表: http://localhost:{self.port}/api/tokens")
            return True
        except Exception as e:
            logger.error(f"❌ 启动HTTP服务器失败: {e}")
            return False
    
    async def stop(self):
        """停止HTTP服务器"""
        # 停止HTTP服务器
        if AIOHTTP_AVAILABLE and self.runner:
            await self.runner.cleanup()
            if self.site:
                await self.site.stop()
            
        self.is_running = False
        logger.info("✅ HTTP服务器已停止")
    
    # 移除所有WebSocket相关方法
    
    async def handle_token_update(self, data: dict, transport: str = "http"):
        """处理Token更新"""
        access_token = data.get("accessToken")
        if not access_token:
            logger.warning(f"⚠️ 收到的Token更新消息中没有accessToken字段 (传输方式: {transport})")
            return
        
        user_info = data.get("user", {})
        user_name = user_info.get("name", "unknown")
        user_email = user_info.get("email", "unknown")
        
        # 存储Token信息
        self.tokens[access_token] = {
            "token": access_token,
            "user_name": user_name,
            "user_email": user_email,
            "expires": data.get("expires"),
            "status": data.get("status", "active"),
            "last_updated": datetime.now().isoformat(),
            "transport": transport,  # 记录传输方式
            "raw_data": data  # 保存原始数据以供调试
        }
        
        logger.info(f"✅ 收到Token更新 ({transport}): {user_name} ({user_email})")
        logger.info(f"🔑 Token长度: {len(access_token)}")
        logger.info(f"📊 当前Token数量: {len(self.tokens)}")
    
    # 移除WebSocket相关方法
    
    async def start_http_server(self):
        """启动HTTP服务器"""
        if not AIOHTTP_AVAILABLE:
            logger.warning("⚠️ aiohttp模块未安装，HTTP服务器无法启动")
            return
            
        try:
            self.app = web.Application()
            self.setup_routes()
            
            self.runner = web.AppRunner(self.app)
            await self.runner.setup()
            
            self.site = web.TCPSite(self.runner, 'localhost', self.port)
            await self.site.start()
            
            logger.info(f"✅ HTTP服务器已启动，端口: {self.port}")
        except Exception as e:
            logger.error(f"❌ 启动HTTP服务器失败: {e}")
    
    def setup_routes(self):
        """设置HTTP路由"""
        self.app.router.add_post('/api/token', self.handle_http_token)
        self.app.router.add_get('/health', self.handle_health_check)
        self.app.router.add_get('/api/tokens', self.handle_get_tokens)
        self.app.router.add_get('/api/stats', self.handle_get_stats)
    
    async def handle_http_token(self, request):
        """处理HTTP Token上报"""
        try:
            data = await request.json()
            
            # 验证必要字段
            if not data.get('accessToken'):
                return web.json_response({
                    'status': 'error',
                    'message': 'Missing accessToken field'
                }, status=400)
            
            # 添加传输方式信息
            data['transport'] = 'http'
            
            # 处理Token更新
            await self.handle_token_update(data, transport='http')
            
            return web.json_response({
                'status': 'success',
                'message': 'Token received successfully',
                'timestamp': datetime.now().isoformat()
            })
            
        except json.JSONDecodeError:
            return web.json_response({
                'status': 'error',
                'message': 'Invalid JSON format'
            }, status=400)
        except Exception as e:
            logger.error(f"❌ 处理HTTP Token时发生错误: {e}")
            return web.json_response({
                'status': 'error',
                'message': f'Internal server error: {str(e)}'
            }, status=500)
    
    async def handle_health_check(self, request):
        """健康检查端点"""
        return web.json_response({
            'status': 'healthy',
            'server': 'TokenHttpServer',
            'timestamp': datetime.now().isoformat(),
            'tokens_count': len(self.tokens),
            'is_running': self.is_running
        })
    
    async def handle_get_tokens(self, request):
        """获取所有Token信息（仅基本信息，不包含完整Token）"""
        token_list = []
        for token_info in self.tokens.values():
            # 不返回完整Token，只返回基本信息
            token_list.append({
                'user_name': token_info.get('user_name'),
                'user_email': token_info.get('user_email'),
                'last_updated': token_info.get('last_updated'),
                'status': token_info.get('status'),
                'transport': token_info.get('transport', 'unknown'),
                'token_preview': token_info.get('token', '')[:8] + '...' if token_info.get('token') else ''
            })
        
        return web.json_response({
            'status': 'success',
            'count': len(token_list),
            'tokens': token_list,
            'timestamp': datetime.now().isoformat()
        })
    
    async def handle_get_stats(self, request):
        """获取服务器统计信息"""
        return web.json_response({
            'status': 'success',
            'stats': {
                'tokens_count': len(self.tokens),
                'server_running': self.is_running,
                'port': self.port,
                'supports_http': AIOHTTP_AVAILABLE
            },
            'timestamp': datetime.now().isoformat()
        })
    
    def get_tokens(self) -> List[str]:
        """获取所有Token列表"""
        return list(self.tokens.keys())
    
    def get_token_info(self, token: str) -> dict:
        """获取指定Token的详细信息"""
        return self.tokens.get(token, {})
    
    def get_all_token_info(self) -> List[dict]:
        """获取所有Token的详细信息"""
        return list(self.tokens.values())
    
    def remove_token(self, token: str) -> bool:
        """移除指定的Token"""
        if token in self.tokens:
            del self.tokens[token]
            logger.info(f"🗑️ 已移除Token: {token[:8]}...")
            return True
        return False
    
    def clear_tokens(self):
        """清空所有Token"""
        count = len(self.tokens)
        self.tokens.clear()
        logger.info(f"🗑️ 已清空所有Token，共{count}个")
    
    # 移除WebSocket相关方法


# 全局HTTP服务器实例
_global_http_server: TokenHttpServer = None


def get_http_server(port: int = 5103) -> TokenHttpServer:
    """获取全局HTTP服务器实例"""
    global _global_http_server
    if _global_http_server is None:
        _global_http_server = TokenHttpServer(port)
    return _global_http_server


async def start_http_server(port: int = 5103) -> bool:
    """启动HTTP服务器"""
    server = get_http_server(port)
    return await server.start()


async def stop_http_server():
    """停止HTTP服务器"""
    global _global_http_server
    if _global_http_server:
        await _global_http_server.stop()
        _global_http_server = None


def is_http_server_running() -> bool:
    """检查HTTP服务器是否正在运行"""
    global _global_http_server
    return _global_http_server is not None and _global_http_server.is_running


def get_auto_tokens() -> List[str]:
    """获取自动获取的Token列表"""
    global _global_http_server
    if _global_http_server:
        return _global_http_server.get_tokens()
    return []


def get_auto_token_info() -> List[dict]:
    """获取自动获取的Token详细信息"""
    global _global_http_server
    if _global_http_server:
        return _global_http_server.get_all_token_info()
    return []


async def refresh_auto_tokens():
    """请求刷新自动获取的Token"""
    # HTTP服务器不需要刷新请求，因为Token是通过HTTP POST主动上报的
    logger.info("🔄 HTTP服务器：Token通过HTTP主动上报，无需发送刷新请求")


# 向后兼容的包装函数
async def start_websocket_server(port: int = 5103) -> bool:
    """向后兼容：启动WebSocket服务器（实际启动HTTP服务器）"""
    logger.warning("⚠️ start_websocket_server已弃用，请使用start_http_server")
    return await start_http_server(port)


async def stop_websocket_server():
    """向后兼容：停止WebSocket服务器（实际停止HTTP服务器）"""
    logger.warning("⚠️ stop_websocket_server已弃用，请使用stop_http_server")
    await stop_http_server()


def is_websocket_server_running() -> bool:
    """向后兼容：检查WebSocket服务器是否正在运行（实际检查HTTP服务器）"""
    logger.warning("⚠️ is_websocket_server_running已弃用，请使用is_http_server_running")
    return is_http_server_running()
