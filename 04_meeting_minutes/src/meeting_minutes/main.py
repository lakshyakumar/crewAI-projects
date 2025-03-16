#!/usr/bin/env python
from random import randint
from pydantic import BaseModel
from crewai.flow import Flow, listen, start
from crews.meeting_minutes.meeting_minutes_crew import MeetingMinutesCrew
from crews.gmailcrew.gmailcrew import GmailCrew
from pathlib import Path
from pydub import AudioSegment
from pydub.utils import make_chunks
import os

from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI
client = OpenAI()


class MeetingMinutesState(BaseModel):
    transcript: str = ""
    meeting_minutes: str = ""


class MeetingMinutesFlow(Flow[MeetingMinutesState]):

    @start()
    def transcribe_meeting(self):
        print("Generating transcription...")
        
        SCRIPT_DIR = Path(__file__).parent
        audio_path = str(SCRIPT_DIR.parent.parent/ "samples" / "EarningsCall.wav")
        audio = AudioSegment.from_file(audio_path, format="wav")
        
        chunk_length_ms = 60000
        chunks = make_chunks(audio, chunk_length_ms)
        

        full_transcription = ""
        for i, chunk in enumerate(chunks):
            print(f"Transcribing chunk {i+1}/{len(chunks)}")
            chunk_path = f"chunk_{i}.wav"
            chunk.export(chunk_path, format="wav")
            
            with open(chunk_path, "rb") as audio_file:
                transcription = client.audio.transcriptions.create(
                    model="whisper-1", 
                    file=audio_file
                )
                full_transcription += transcription.text + " "

        self.state.transcript = full_transcription
        print(f"Transcription: {self.state.transcript}")

    @listen(transcribe_meeting)
    def generate_meeting_minutes(self):
        print("Generating Meeting Minutes")

        crew = MeetingMinutesCrew()

        inputs = {
            "transcript": self.state.transcript
        }
        meeting_minutes = crew.crew().kickoff(inputs)
        self.state.meeting_minutes = meeting_minutes
        
        print(f"Meeting Minutes: {self.state.meeting_minutes}")

    @listen(generate_meeting_minutes)
    def create_draft_meeting_minutes(self):
        print("Creating Draft Meeting Minutes")

        crew = GmailCrew()

        inputs = {
            "body": str(self.state.meeting_minutes)
        }

        draft_crew = crew.crew().kickoff(inputs)
        print(f"Draft Crew: {draft_crew}")


def kickoff():
    meeting_minutes_flow = MeetingMinutesFlow()
    meeting_minutes_flow.kickoff()




if __name__ == "__main__":
    kickoff()
