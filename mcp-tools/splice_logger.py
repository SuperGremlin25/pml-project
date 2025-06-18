#!/usr/bin/env python3
import argparse
import requests
import os
import sys
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'infra', '.env'))

API_URL = os.getenv("API_URL", "http://localhost:8000")
VALID_SPLICE_TYPES = ["fusion", "mechanical", "preconnectorized"]

def validate_splice_type(splice_type: str) -> str:
    if splice_type.lower() not in VALID_SPLICE_TYPES:
        raise ValueError(f"Invalid splice type. Must be one of: {', '.join(VALID_SPLICE_TYPES)}")
    return splice_type.lower()

def main():
    parser = argparse.ArgumentParser(
        description="Log a fiber splice operation",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument("--crew", required=True, help="Name of the crew performing the splice")
    parser.add_argument("--segment", required=True, help="Segment identifier where splice was performed")
    parser.add_argument("--type", required=True, choices=VALID_SPLICE_TYPES, help="Type of splice performed")
    parser.add_argument("--timestamp", default=datetime.now().isoformat(), 
                       help="Timestamp of the splice (ISO format)")
    parser.add_argument("--notes", default="", help="Additional notes about the splice")

    args = parser.parse_args()

    try:
        payload = {
            "crew_name": args.crew,
            "segment_id": args.segment,
            "splice_type": validate_splice_type(args.type),
            "timestamp": args.timestamp,
            "notes": args.notes
        }

        response = requests.post(f"{API_URL}/api/splice", json=payload)
        response.raise_for_status()
        result = response.json()
        
        print("✅ Splice logged successfully:")
        print(f"Crew: {payload['crew_name']}")
        print(f"Segment: {payload['segment_id']}")
        print(f"Type: {payload['splice_type']}")
        print(f"Timestamp: {payload['timestamp']}")
        if payload['notes']:
            print(f"Notes: {payload['notes']}")

    except requests.exceptions.ConnectionError:
        print(f"❌ Error: Could not connect to the API at {API_URL}")
        print("Please check if the server is running and the API_URL is correct")
        sys.exit(1)
    except requests.exceptions.HTTPError as e:
        print(f"❌ Error: API request failed with status {e.response.status_code}")
        print(f"Details: {e.response.json().get('detail', 'Unknown error')}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
