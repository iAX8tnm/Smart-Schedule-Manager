console.log('本次请求意图来自'+eventName);
//console.log(context);

for (var i in event.request.slots) {
    slot = event.request.slots[i];
    if (slot.name == 'time') {
        event.session.properties.norm_time = slot.normValue;
        event.session.properties.time = slot.value;
    } else if (slot.name == "people") {
        event.session.properties.people = slot.value;
    }
}

function query_other_schedule_with_time() {
    console.log('正在查询行程，人物：' + event.session.properties.people + ' 时间：' + event.session.properties.norm_time + '的行程');
    response.end('这是' + event.session.properties.people + event.session.properties.time + '的行程');
}

function query_other_schedule_without_time() {
    response.speak('请问您想查询' + event.request.slots[0].value + '什么时候的行程？');
}

function query_other_add_time() {
    if (event.session.properties.norm_time != null) {
        query_other_schedule_with_time()
    } else {
        response.speak('请问您想查询' + event.session.properties.people + '什么时候的行程？');
    }
    
}

if (eventName == 'query_other_schedule_with_time') {
    query_other_schedule_with_time();
} else if (eventName == 'query_other_schedule_without_time') {
    query_other_schedule_without_time();
} else if (eventName == 'query_other_add_time') {
    query_other_add_time();
} else {
    response.error('Ooooops something wrong', event);
}