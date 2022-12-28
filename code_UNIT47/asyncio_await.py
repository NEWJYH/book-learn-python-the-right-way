import asyncio

async def add(a, b):
    print(f'add : {a} + {b}')
    await asyncio.sleep(1.0) # 1초 대기, asyncio.sleep도 네이티브 코루틴
    return a + b

async def print_add(a, b):
    result = await add(a, b) # await로 다른 네이티브 코루틴 실행
                             # 반환값을 변수에 저장
    print(f'print_add : {a} + {b} = {result}')

loop = asyncio.get_event_loop() # 이벤트 루프를 얻음
loop.run_until_complete(print_add(1, 2)) # print_add가 끝날 때까지 이벤트 루프를 실행
loop.close() # 이벤트 루프를 닫음