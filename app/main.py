from fastapi import Depends, FastAPI
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from sqladmin import ModelView
from app.db import get_session, engine
from app.models.main import Song, SongCreate, SongBase
from sqladmin import Admin

app = FastAPI()
admin = Admin(app, engine)


@app.get("/ping")
async def pong():
    return {"ping": "pong!"}


@app.get("/songs", response_model=list[Song])
async def get_songs(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Song))
    songs = result.scalars().all()
    return [Song(name=song.name, artist=song.artist, id=song.id) for song in songs]


@app.post("/songs")
async def add_song(song: SongCreate, session: AsyncSession = Depends(get_session)):
    song = Song(name=song.name, artist=song.artist)
    session.add(song)
    await session.commit()
    await session.refresh(song)
    return song



class SongAdmin(ModelView, model=Song):
    column_list = '__all__'


admin.add_view(SongAdmin)