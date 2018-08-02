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

function time() { 
    if (event.session.properties.thing != null) { //判断一下是不是直接说了个时间，防止没有thing就回答了
        add_schedule_with_time()
    } else {
        response.error('Ooooops something wrong', event);
    }
}

if (eventName == 'add_schedule_with_time') {
    add_schedule_with_time();
} else if (eventName == 'add_schedule_without_time') {
    add_schedule_without_time();
} else if (eventName == 'time') {
    time();
} else {
    Response.error('Ooooops something wrong', event)
}