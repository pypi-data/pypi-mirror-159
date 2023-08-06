from bs4 import BeautifulSoup
from requests import get

from util.config import get_config
from util.utils import format_output, cast, listify, run_thread, compact_list


def affiliation(affiliation_ids, output_format='dict'):
    result = run_thread(worker, listify(affiliation_ids))
    result = compact_list(result)

    return format_output(result, output_format)


def worker(affiliation_id, worker_result):
    domain = get_config()['domain']
    url = f'{domain}/affiliations/profile/{affiliation_id}'
    html = BeautifulSoup(get(url).content, 'html.parser')

    # profile section
    name = html.select('.univ-name > h3')[0].text.strip()
    abbrv_name = html.select('.affil-abbrev')[0].text.strip()
    location = html.select('.affil-loc')[0].text.strip()
    code = html.select('.affil-code')[0].text.split(':')[-1].strip()

    # stats section
    stat_profile = html.select('.affil-profile-card .stat-num')
    stat_names = 'authors', 'departments', 'journals'
    stat_int = [cast(stat_profile[i].text.replace('.', '')) for i in range(3)]
    stats = dict(zip(stat_names, stat_int))

    # sinta score section
    score_soup = html.select('.stat-profile .pr-num')
    score_names = 'overall', '3_years', 'productivity', 'productivity_3_years'
    score_numbers = [cast(score_soup[i].text.replace('.', '')) for i in range(4)]
    sinta_scores = dict(zip(score_names, score_numbers))

    # indexer section
    index_stats = {}
    index_rows = html.select('.stat-table > tbody > tr')
    index_aspects = 'articles', 'citations', 'cited_documents', 'citation_per_researcher'
    indexers = 'scopus', 'scholar', 'wos', 'garuda'

    last_update = html.select('small')[-1].text.split(' :')[1]

    for i, row in enumerate(index_rows):
        numbers = [cast(row.select('td')[i].text.replace('.', '').replace(',', '.')) for i in range(1, 5)]
        index_stats[index_aspects[i]] = dict(zip(indexers, numbers))

    result_data = {
                      'id': affiliation_id,
                      'code': code,
                      'url': url,
                      'name': name,
                      'abbreviation': abbrv_name,
                      'location': location,
                      'sinta_score': sinta_scores,
                      'last_update': last_update
                  } | stats | index_stats

    worker_result.append(result_data)
