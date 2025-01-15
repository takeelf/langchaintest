from dotenv import load_dotenv
import requests

load_dotenv()

def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False):
    if mock:
        linkedin_profile_url = "https://gist.githubusercontent.com/takeelf/123e7d30b91ba7b2003802229088226d/raw/d4916ded3ea39fdd4b1a24383717c77b6b07a016/wonho-choi.json"
        response = requests.get(linkedin_profile_url, timeout=10)
    else:
        linkedin_profile_url = "https://gist.githubusercontent.com/takeelf/123e7d30b91ba7b2003802229088226d/raw/d4916ded3ea39fdd4b1a24383717c77b6b07a016/wonho-choi.json"
        response = requests.get(linkedin_profile_url, timeout=10)
    data = response.json()
    
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
        and k not in ["people_alse_viewed", "certifications"]
    }
    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")
    
    return data

if __name__ == "__main__":
    print(
        scrape_linkedin_profile(
            linkedin_profile_url="https://linkedin.com/in/wonho-choi-768a88b7/",
            mock=True
        )
    )