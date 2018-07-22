console.log('本次请求意图来自'+eventName);
//console.log(context);

for (var i in event.request.slots) {
    slot = event.request.slots[i];
    if (slot.name == 'time') {
        event.session.properties.time = slot.normValue;
    }
}

function query_schedule_with_time() {
    console.log('正在查询行程，时间：' + event.session.properties.time + '的行程');
    response.end('这是你' + event.request.slots[0].value + '的行程');
}

function query_schedule_without_time() {
    response.speak('请问您想查询什么时候的行程？');
}

function time() {
    if (event.session.properties.time != null) {
        query_schedule_with_time()
    } else {
        response.speak('请问您想查询什么时候的行程？');
    }
    
}

if (eventName == 'query_schedule_with_time') {
    query_schedule_with_time();
} else if (eventName == 'query_schedule_without_time') {
    query_schedule_without_time();
} else if (eventName == 'time') {
    time();
} else {
    response.error('Ooooops something wrong', event);
}