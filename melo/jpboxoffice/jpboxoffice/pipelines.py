# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import datetime

class JpboxofficePipeline:
    def process_item(self, item, spider):

        # item['titre'] = item['titre'].strip()
        # item['pays'] = item['pays'].strip()
        # item['genre'] = item['genre'].strip()
        # item['studio'] = item['studio'].strip()
        # item['entrees_premiere_semaine'] = item['entrees_premiere_semaine'].strip()
        # item['salles_premiere_semaine'] = item['salles_premiere_semaine'].strip()
        # item['acteurs'] = [acteur.strip() for acteur in item['acteurs']]
        
        # if item['date']:
        #     item['date'] = datetime.datetime.strptime(item['date'].strip(), "%d/%m/%Y").strftime("%Y-%m-%d")
        
        # #verifie si producteur contient une valeur avant de strip
        # if item['producteur']:
        #     item['producteur'] = item['producteur'].strip()
      
        # item['realisateur'] = ''.join(item['realisateur'])
        # item['realisateur'] = item['realisateur'].lstrip()

        # item['budget'] = item['budget'].replace(' ', '')  # Enlève tous les espaces
        # item['budget'] = item['budget'].replace('$', '')  # Enlève le symbole $
        # item['budget'] = item['budget'].replace('€', '')

        # item['budget'] = int(item['budget'])
        # item['entrees_premiere_semaine'] = int(item['entrees_premiere_semaine'])
        # item['salles_premiere_semaine'] = int(item['salles_premiere_semaine'])
        
        return item