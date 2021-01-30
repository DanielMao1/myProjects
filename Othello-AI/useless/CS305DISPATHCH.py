import socket, asyncio

async def dispatch(reader, writer):
        while True:
            try:
                data = await reader.readline()
                message = data.decode().split(' ')
                if data == b'quit\r\n':
                    writer.writelines([b'ok'])
                    break
            except TypeError:
                pass
            print(message)
            writer.writelines([data])
            await writer.drain()
        writer.close()





if __name__ == "__main__":
 try:
     loop = asyncio.get_event_loop()
     coro = asyncio.start_server(dispatch, '127.0.0.1', 1081, loop=loop)
     server = loop.run_until_complete(coro)
     # Serve requests until Ctrl+C is pressed
     print('Serving on {}'.format(server.sockets[0].getsockname()))
     try:
         loop.run_forever()
     except KeyboardInterrupt:
         pass
     # Close the server
     server.close()
     loop.run_until_complete(server.wait_closed())
     loop.close()
 except KeyboardInterrupt:
    pass