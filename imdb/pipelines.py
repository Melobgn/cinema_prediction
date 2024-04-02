from itemadapter import ItemAdapter
import re
from scrapy.exceptions import DropItem

class AllocFilmPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        
        entrees = adapter.get('entrees')
        adapter['entrees'] = int(entrees)
        # Nettoyage du champ 'duree'
        if 'duree' in adapter:
            duree_clean = self.nettoyer_duree(adapter['duree'])
            if duree_clean is not None:
                adapter['duree'] = duree_clean
            else:
                spider.logger.info(f"Durée non valide pour: {adapter['titre']}")
                raise DropItem(f"Durée non valide pour: {adapter['titre']}")

        # Suppression du premier acteur si la liste 'acteurs' n'est pas vide
        if adapter.get('acteurs'):
            adapter['acteurs'].pop(0)

        # Suppression du premier réalisateur si la liste 'realisateur' n'est pas vide
        if adapter.get('realisateur'):
            adapter['realisateur'].pop(0)

        # Suppression des trois premiers genres si la liste 'genre' a au moins trois éléments
        if adapter.get('genre'):
            adapter['genre'] = adapter['genre'][3:] if len(adapter['genre']) >= 3 else adapter['genre']

        
        # field 'pays'
        if 'pays' in adapter:
            adapter['pays'] = adapter['pays'].strip()

        # field 'anecdotes'
        if 'anecdotes' in adapter:
            anecdotes_text = adapter['anecdotes']
            match = re.search(r'\d+', anecdotes_text)
            adapter['anecdotes'] = int(match.group()) if match else 0

        # field 'studio'
        if 'studio' in adapter:
            adapter['studio'] = adapter['studio'].strip()
            
        return item

    def nettoyer_duree(self, duree_list):
        if isinstance(duree_list, list):
            duree_str = ''.join(duree_list).replace('\n', '').strip()
        elif isinstance(duree_list, str):
            duree_str = duree_list.replace('\n', '').strip()
        else:
            return None

        match = re.search(r'(\d+)h\s*(\d+)?', duree_str)
        if match:
            heures = int(match.group(1))
            minutes = int(match.group(2)) if match.group(2) else 0
            return heures * 60 + minutes
        return None
