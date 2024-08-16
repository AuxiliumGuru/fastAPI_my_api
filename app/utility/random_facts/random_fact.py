import requests


class Fact:

    @staticmethod
    def get_random_fact():
        try:
            response = requests.get('https://uselessfacts.jsph.pl/random.json?language=en')
            response.raise_for_status()
            return response.json()['text']
        except requests.RequestException as e:
            return f"An error occurred: {str(e)}"

    @staticmethod
    def get_today_random_fact():
        try:
            response = requests.get('https://uselessfacts.jsph.pl/today.json?language=en')
            response.raise_for_status()
            return response.json()['text']
        except requests.RequestException as e:
            return f"An error occurred: {str(e)}"


if __name__ == '__main__':
    facts = Fact()
    print(facts.get_random_fact())
    print(facts.get_today_random_fact())


