import sys
import requests
from feed import feed
from models.release_notes import ReleaseNote
from bs4 import BeautifulSoup
from sqlmodel import SQLModel, Session,create_engine,select

release_notes_path = "https://docs.snowflake.com/ja/release-notes/"
release_notes_url = f"{release_notes_path}/new-features"
sqlite3_path = "/app/db/test.db"
sqlite3_url = f"sqlite:///{sqlite3_path}"
rss_path = "/app/dist/sf_release_notes.xml"

def main()->int:
    response = requests.get(release_notes_url)
    soup = BeautifulSoup(response.text,'html.parser')
    engine = create_engine(sqlite3_url, echo=False)
    num_new = 0
    with Session(engine) as session:
        #テーブルが無い場合に作成する
        SQLModel.metadata.create_all(engine)

        #過去に取得済みのリリースノートのタイトルを取得する
        release_notes = session.exec(select(ReleaseNote).order_by(ReleaseNote.created_at)).all()
        titles = [release_note.title for release_note in release_notes]

        #今回取得したリリースノートが過去に取得済みでなければ永続化する
        for element in soup.select('li.toctree-l1 >a'):
            title = element.getText()
            if title in titles:
                continue
            release_note = ReleaseNote()
            release_note.title = title
            release_note.url = f"{release_notes_path}/{element['href']}"
            session.add(release_note)
            num_new += 1
        session.commit()

        #RSSを作る
        if len(release_notes) > 0:
            entries = "".join([(release_note.getEntryString(session)) for release_note in release_notes])
            s = feed.format(updated_at=release_notes[0].created_at.isoformat(),entries=entries)
            with open(rss_path,'w') as f:
                f.write(s)
        
        #標準出力
        print(f"{num_new} added.")

    return 0

if __name__ == '__main__':
    sys.exit(main())  # next section explains the use of sys.exit