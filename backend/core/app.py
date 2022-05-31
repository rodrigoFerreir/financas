from fastapi import FastAPI
from routes.UserRoutes import router as UserRoutes
from routes.AuthRoutes import router as AuthRoutes
from routes.AccountRoutes import router as AccountRoutes

app = FastAPI()

app.include_router(AccountRoutes, tags=['Lançamentos'], prefix='/api/account')
app.include_router(UserRoutes, tags=['Usuarios'], prefix='/api/user')
app.include_router(AuthRoutes, tags=['Autenticação'], prefix='/api/auth')


@app.get('/api/health', tags=['Health'])
async def health():
    return {
        'status': 'ok'
    }
