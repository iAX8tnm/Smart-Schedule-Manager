console.log('本次请求意图来自'+eventName);

function shutdown() {
    console.log("正在退出程序")
    response.end("正在关机")
}

if (eventName == 'command_shutdown') {
    shutdown()
} else {
    response.error('Ooooops something wrong', event);
}