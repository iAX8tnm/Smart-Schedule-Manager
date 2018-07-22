console.log('本次请求意图来自'+eventName);
//console.log(context);

for (var i in event.request.slots) {
    slot = event.request.slots[i];

    if (slot.name == 'thing') {
        event.session.properties.thing = slot.normValue;
    }
    if (slot.name == 'time') {
        event.session.properties.time = slot.value;
    }
}

function add_schedule_with_time() {
    console.log('添加新的日程:' + event.session.properties.thing);
    response.end('好的，' + event.session.properties.time + '提醒您' + event.session.properties.thing);
}

function add_schedule_without_time() {
    response.speak('好的，请问什么时候提醒您' + event.session.properties.thing);
}

function time() {  //所以他好像没什么用
    if (event.session.properties.time != null) { // 这个条件也是直接为true
        add_schedule_with_time()
    } else {//这个else 应该不会进去，可删
        response.speak('请问您想查询什么时候的行程？');
        console.log('3333333333')
    }
}

if (eventName == 'add_schedule_with_time') {
    add_schedule_with_time();
} else if (eventName == 'add_schedule_without_time') {
    add_schedule_without_time();
} else if (eventName == 'time') {
    add_schedule_with_time();
} else {
    Response.error('Ooooops something wrong', event)
}