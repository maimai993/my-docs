// ==UserScript==
// @name         ChatGPT AccessToken HTTP 上报 (纯HTTP版本)
// @namespace    http://tampermonkey.net/
// @version      2.0
// @description  提取accessToken并通过HTTP POST上报到 http://localhost:5103/api/token (解决CSP问题)
// @author       maimai
// @match        https://chatgpt.com/*
// @grant        GM_xmlhttpRequest
// @grant        GM_log
// @grant        GM_notification
// @grant        GM_setValue
// @grant        GM_getValue
// @grant        unsafeWindow
// @connect      localhost
// @connect      127.0.0.1
// @run-at       document-start
// ==/UserScript==

(function() {
    'use strict';
    
    // 配置
    const HTTP_URL = 'http://localhost:5103/api/token'; // HTTP端点
    const REFRESH_INTERVAL = 10 * 60 * 1000; // 10分钟
    const RETRY_INTERVAL = 5000; // 重试间隔
    let isConnected = false;
    let reconnectAttempts = 0;
    const MAX_RECONNECT_ATTEMPTS = 10;
    let refreshTimer = null;

    // 1. HTTP 连接管理
    function connectHttp() {
        console.log('[Token HTTP] 🔗 正在连接HTTP服务器...');
        
        isConnected = false;
        
        // 立即提取并发送Token
        extractAndSendTokenViaHTTP();
        
        // 设置定时刷新
        startRefreshTimer();
        
        // 标记为已连接
        isConnected = true;
        reconnectAttempts = 0;
        console.log('[Token HTTP] ✅ HTTP连接初始化完成');
    }

    // 2. 发送Token到HTTP服务器
    function sendTokenViaHTTP(tokenData) {
        console.log('[Token HTTP] 📡 发送Token数据到HTTP端点...');
        
        // 准备HTTP数据
        const httpData = {
            accessToken: tokenData.accessToken,
            user: tokenData.user,
            account: tokenData.account,
            expires: tokenData.expires,
            status: tokenData.status,
            timestamp: tokenData.timestamp,
            transport: 'http'
        };
        
        GM_xmlhttpRequest({
            method: 'POST',
            url: HTTP_URL,
            headers: {
                'Content-Type': 'application/json'
            },
            data: JSON.stringify(httpData),
            timeout: 10000,
            onload: function(response) {
                if (response.status >= 200 && response.status < 300) {
                    console.log('[Token HTTP] ✅ Token发送成功:', response.status, response.responseText);
                    isConnected = true;
                    reconnectAttempts = 0;
                    
                    // 显示成功通知
                    showSuccessNotification(tokenData.user.name, tokenData.accessToken.length);
                } else {
                    console.log('[Token HTTP] ⚠️ 服务器返回错误:', response.status, response.responseText);
                    isConnected = false;
                    
                    GM_notification({
                        title: '⚠️ HTTP服务器错误',
                        text: `服务器返回错误: ${response.status}`,
                        timeout: 5000
                    });
                    
                    // 重试
                    if (reconnectAttempts < MAX_RECONNECT_ATTEMPTS) {
                        reconnectAttempts++;
                        console.log(`[Token HTTP] 🔄 ${RETRY_INTERVAL/1000}秒后重试 (${reconnectAttempts}/${MAX_RECONNECT_ATTEMPTS})...`);
                        setTimeout(extractAndSendTokenViaHTTP, RETRY_INTERVAL);
                    }
                }
            },
            onerror: function(error) {
                console.log('[Token HTTP] ❌ 发送失败:', error.statusText);
                isConnected = false;
                
                GM_notification({
                    title: '❌ HTTP连接失败',
                    text: `无法连接到HTTP服务器: ${error.statusText}`,
                    timeout: 5000
                });
                
                // 重试
                if (reconnectAttempts < MAX_RECONNECT_ATTEMPTS) {
                    reconnectAttempts++;
                    console.log(`[Token HTTP] 🔄 ${RETRY_INTERVAL/1000}秒后重试 (${reconnectAttempts}/${MAX_RECONNECT_ATTEMPTS})...`);
                    setTimeout(extractAndSendTokenViaHTTP, RETRY_INTERVAL);
                }
            },
            ontimeout: function() {
                console.log('[Token HTTP] ⏱️ 请求超时');
                isConnected = false;
                
                GM_notification({
                    title: '⏱️ HTTP请求超时',
                    text: 'HTTP请求超时，服务器可能未运行',
                    timeout: 5000
                });
                
                // 重试
                if (reconnectAttempts < MAX_RECONNECT_ATTEMPTS) {
                    reconnectAttempts++;
                    console.log(`[Token HTTP] 🔄 ${RETRY_INTERVAL/1000}秒后重试 (${reconnectAttempts}/${MAX_RECONNECT_ATTEMPTS})...`);
                    setTimeout(extractAndSendTokenViaHTTP, RETRY_INTERVAL);
                }
            }
        });
    }

    // 3. 心跳机制（HTTP不需要心跳，但可以定期检查连接）
    function checkConnection() {
        if (!isConnected) {
            console.log('[Token HTTP] 🔍 检查连接状态...');
            extractAndSendTokenViaHTTP();
        }
    }

    // 4. 定时刷新
    function startRefreshTimer() {
        stopRefreshTimer(); // 先停止已有的
        
        refreshTimer = setInterval(() => {
            console.log('[Token HTTP] ⏰ 10分钟定时刷新，重新获取Token...');
            GM_notification({
                title: '定时刷新',
                text: '10分钟到期，重新获取Token',
                timeout: 3000
            });
            location.reload();
        }, REFRESH_INTERVAL);
    }

    function stopRefreshTimer() {
        if (refreshTimer) {
            clearInterval(refreshTimer);
            refreshTimer = null;
        }
    }

    // 5. 提取并发送Token
    function extractAndSendTokenViaHTTP() {
        console.log('[Token HTTP] 🔍 开始提取Token...');
        
        GM_xmlhttpRequest({
            method: 'GET',
            url: 'https://chatgpt.com/api/auth/session',
            timeout: 10000,
            onload: function(response) {
                try {
                    const data = JSON.parse(response.responseText);
                    
                    if (data && data.accessToken && data.user) {
                        const tokenData = {
                            type: 'token_update',
                            timestamp: new Date().toISOString(),
                            accessToken: data.accessToken,
                            user: {
                                id: data.user.id,
                                name: data.user.name,
                                email: data.user.email
                            },
                            account: data.account,
                            expires: data.expires,
                            status: 'active'
                        };
                        
                        // 发送到HTTP服务器
                        sendTokenViaHTTP(tokenData);
                    } else {
                        handleNoToken('会话数据中未找到Token或用户信息');
                    }
                } catch (e) {
                    handleNoToken('解析会话数据失败: ' + e.message);
                }
            },
            onerror: function(error) {
                handleNoToken('请求会话接口失败: ' + error.statusText);
            },
            ontimeout: function() {
                handleNoToken('请求会话接口超时');
            }
        });
    }

    // 6. 处理无Token情况
    function handleNoToken(reason) {
        console.log('[Token HTTP] ⚠️ Token获取失败:', reason);
        
        // 显示错误通知
        GM_notification({
            title: '❌ 登录过期',
            text: reason,
            timeout: 5000
        });
        
        // 10秒后重试
        setTimeout(extractAndSendTokenViaHTTP, 10000);
    }

    // 7. 显示成功通知
    function showSuccessNotification(username, tokenLength) {
        GM_notification({
            title: '✅ Token获取成功',
            text: `用户: ${username} | Token长度: ${tokenLength}`,
            timeout: 4000
        });
        
        // 在控制台显示详细信息
        console.log('[Token HTTP] 🎉 Token上报成功!');
        console.log('[Token HTTP] 📊 下一次刷新: 10分钟后');
        console.log('[Token HTTP] 🔄 自动刷新倒计时已启动');
    }

    // 8. 页面控制台命令
    function setupConsoleCommands() {
        unsafeWindow.tokenHTTP = {
            // 手动提取并发送Token
            refreshToken: function() {
                console.log('[Token HTTP] 🔄 手动刷新Token...');
                extractAndSendTokenViaHTTP();
            },
            
            // 检查连接状态
            status: function() {
                return {
                    connected: isConnected,
                    reconnectAttempts: reconnectAttempts,
                    nextRefresh: refreshTimer ? 'active' : 'inactive',
                    serverUrl: HTTP_URL
                };
            },
            
            // 手动重连
            reconnect: function() {
                console.log('[Token HTTP] 🔗 手动重连HTTP服务器...');
                reconnectAttempts = 0;
                connectHttp();
            },
            
            // 手动刷新页面
            reloadPage: function() {
                console.log('[Token HTTP] 🔄 手动刷新页面...');
                location.reload();
            },
            
            // 诊断连接问题
            diagnoseConnection: function() {
                console.log('[Token HTTP] 🔍 诊断连接问题...');
                console.log('[Token HTTP] 当前URL:', window.location.href);
                console.log('[Token HTTP] Tampermonkey版本:', GM_info ? GM_info.version : '未知');
                console.log('[Token HTTP] 脚本权限:', GM_info ? GM_info.script.grants : '未知');
                console.log('[Token HTTP] @connect指令:', GM_info ? GM_info.script.connect : '未知');
                
                // 测试HTTP连接
                GM_xmlhttpRequest({
                    method: 'GET',
                    url: 'http://localhost:5103/health',
                    timeout: 5000,
                    onload: function(response) {
                        console.log('[Token HTTP] ✅ HTTP测试成功:', response.status, response.responseText);
                    },
                    onerror: function(error) {
                        console.log('[Token HTTP] ❌ HTTP测试失败:', error.statusText);
                    }
                });
            },
            
            // 测试Token提取
            testTokenExtraction: function() {
                console.log('[Token HTTP] 🔍 测试Token提取...');
                extractAndSendTokenViaHTTP();
            }
        };
        
        console.log('[Token HTTP] 🎮 控制台命令已启用:');
        console.log('   tokenHTTP.refreshToken() - 手动刷新Token');
        console.log('   tokenHTTP.status() - 查看连接状态');
        console.log('   tokenHTTP.reconnect() - 手动重连');
        console.log('   tokenHTTP.reloadPage() - 手动刷新页面');
        console.log('   tokenHTTP.diagnoseConnection() - 诊断连接问题');
        console.log('   tokenHTTP.testTokenExtraction() - 测试Token提取');
    }

    // 9. 主函数
    function main() {
        console.clear();
        console.log('══════════════════════════════════════════════════════════');
        console.log('   ChatGPT Token HTTP 上报服务 v2.0 (纯HTTP版本)        ');
        console.log('══════════════════════════════════════════════════════════');
        console.log('');
        console.log('🌐 HTTP服务器:', HTTP_URL);
        console.log('⏰ 自动刷新间隔: 10分钟');
        console.log('🔧 @connect指令: localhost, 127.0.0.1');
        console.log('');
        console.log('📡 工作流程:');
        console.log('   1. 连接HTTP服务器');
        console.log('   2. 自动提取Token并通过HTTP POST上报');
        console.log('   3. 10分钟后自动刷新重新获取');
        console.log('   4. 获取失败上报"登录过期"');
        console.log('');
        console.log('🚀 正在启动服务...');
        console.log('══════════════════════════════════════════════════════════');
        
        // 设置控制台命令
        setupConsoleCommands();
        
        // 连接HTTP服务器
        setTimeout(connectHttp, 1000);
    }

    // 10. 页面卸载清理
    window.addEventListener('beforeunload', function() {
        console.log('[Token HTTP] 🧹 页面卸载，清理资源...');
        stopRefreshTimer();
    });

    // 启动服务
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', main);
    } else {
        main();
    }

})();
