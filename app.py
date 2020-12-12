from aiohttp import web
import json

routes = web.RouteTableDef()

count = 0


@routes.get('/')
async def demo(request):
    print('Test API Executed Successfully')
    response_obj = {'message' : 'Test API Executed Successfully' }
    return web.Response(text=json.dumps(response_obj))


@routes.post('/incActiveUsers')
async def inc_active_user(request):
    try:
        global count
        data = await request.json()
        get_count = data["delta"]
        if get_count == 1:
            count += 1
            response_obj = {'success': True }
            return web.Response(text=json.dumps(response_obj), status=200)
        else:
            response_obj = {'success': False }
            return web.Response(text=json.dumps(response_obj), status=200)

    except Exception as e:
        response_obj = {'status' : 'failed', 'reason': str(e) }
        return web.Response(text=json.dumps(response_obj), status=500)


@routes.post('/decActiveUsers')
async def dec_active_user(request):
    try:
        global count
        data = await request.json()
        get_count = data["delta"]
        if get_count == 1:
            count -= 1
            response_obj = {'success': True }
            return web.Response(text=json.dumps(response_obj), status=200)
        else:
            response_obj = {'success': False }
            return web.Response(text=json.dumps(response_obj), status=200)

    except Exception as e:
        response_obj = {'status' : 'failed', 'reason': str(e) }
        return web.Response(text=json.dumps(response_obj), status=500)


@routes.get('/getActiveUsers')
async def get_active_user(request):
    global count
    if count > 0:
        response_obj = {'numActiveUsers' : count}
        return web.Response(text=json.dumps(response_obj))
    else:
        count = 0
        response_obj = {'numActiveUsers' : count}
        return web.Response(text=json.dumps(response_obj))

    
app = web.Application()
app.router.add_routes(routes)
web.run_app(app, port = 8000, host = "0.0.0.0")