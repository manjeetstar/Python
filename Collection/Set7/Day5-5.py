import asyncio

async def work(n):
    await asyncio.sleep(1)
    print(n)

async def main():
    await asyncio.gather(
        work(1),
        work(2),
        work(3)
    )

asyncio.run(main())

