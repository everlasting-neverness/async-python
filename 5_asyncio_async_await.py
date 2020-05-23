import asyncio


# python 3.4 syntax
@asyncio.coroutine
def print_nums():
    num = 1
    while True:
        print(num)
        num += 1
        yield from asyncio.sleep(0.1)

# python 3.5 syntax
async def print_time():
    count = 1
    while True:
        if count % 3 == 0:
            print('{} seconds have passed'.format(count))
        count += 1
        await asyncio.sleep(1)

@asyncio.coroutine
async def main():
    # python < 3.6 syntax
    # task1 = asyncio.ensure_future(print_nums())
    # task2 = asyncio.ensure_future(print_time())

    task1 = asyncio.create_task(print_nums())
    task2 = asyncio.create_task(print_time())

    await asyncio.gather(task1, task2)


if __name__ == "__main__":
    # python < 3.7 syntax
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(main())
    # loop.close()
    
    asyncio.run(main())