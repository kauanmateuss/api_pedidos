from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

from app.core.settings import settings

engine = create_async_engine(settings.DATABASE_URL)

# FUNCAO PARA PEGAR UMA SESSAO DE CONEXAO COM O BANCO DE DADOS
async def get_session():
    async with AsyncSession(engine, expire_on_commit=False) as session:
        yield session

