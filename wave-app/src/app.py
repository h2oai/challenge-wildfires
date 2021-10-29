from h2o_wave import main, app, Q, ui

@app('/', mode='unicast')
async def serve(q: Q):
    if not q.app.initialized:
        await init_app(q)
        q.app.initialized = True
    
    if not q.client.initialized:
        await init_client(q)
        q.client.initialized = True

async def init_client(q: Q):
    pass

async def init_app(q:Q):
    pass
