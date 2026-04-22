from dotenv import load_dotenv
load_dotenv()

from fake_news_crew.crew import FakeNewsCrew

def run():
    input_date = {
        'subiect': 'S-a descoperit un tratament miraculos și secret pentru cancer folosind apă caldă cu lămâie pe stomacul gol.'
    }

    FakeNewsCrew().crew().kickoff(inputs=input_date)

if __name__=='__main__':
    run()
    