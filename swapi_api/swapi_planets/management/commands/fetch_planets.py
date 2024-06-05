import requests
from django.core.management.base import BaseCommand
from swapi_planets.models import Planet

class Command(BaseCommand):
    help = 'Fetches Planet data from the SWAPI API'

    def handle(self, *args, **options):
        query = """
        query Query {
            allPlanets {
                planets {
                    name
                    population
                    terrains
                    climates
                }
            }
        }
        """
        url = 'https://swapi-graphql.netlify.app/.netlify/functions/index'
        response = requests.post(url, json={'query': query})
        data = response.json()['data']['allPlanets']['planets']

        for planet_data in data:
            Planet.objects.update_or_create(
                name=planet_data['name'],
                defaults={
                    'population': planet_data.get('population', 'unknown'),
                    'terrains': ', '.join(planet_data.get('terrains', [])),
                    'climates': ', '.join(planet_data.get('climates', [])),
                }
            )