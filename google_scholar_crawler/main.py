"""Fetch Google Scholar citation stats into results/gs_data.json.

Behaviour:
- Reads GOOGLE_SCHOLAR_ID from the environment.
- If SERP_API_KEY is set, routes requests through SerpAPI (reliable,
  free tier is enough for a daily run); otherwise fetches directly
  with retries.
- On fetch failure keeps the previous results (restored from the
  google-scholar-stats branch by the workflow) and exits 0, so the
  scheduled job stays green and simply retries the next day.
- Skips rewriting when nothing but the timestamp changed, so the
  workflow can skip empty commits.
"""
import json
import os
import sys
from datetime import datetime

from scholarly import scholarly

RESULTS_DIR = 'results'
DATA_FILE = os.path.join(RESULTS_DIR, 'gs_data.json')
SHIELDS_FILE = os.path.join(RESULTS_DIR, 'gs_data_shieldsio.json')


def fetch_author(scholar_id):
    scholarly.set_timeout(3)  # seconds between requests, be polite
    scholarly.set_retries(5)

    api_key = os.environ.get('SERP_API_KEY')
    if api_key:
        from scholarly import ProxyGenerator
        proxy_generator = ProxyGenerator()
        proxy_generator.SerpAPI(api_key)
        scholarly.use_proxy(proxy_generator)

    author = scholarly.search_author_id(scholar_id)
    scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
    return author


def main():
    scholar_id = os.environ['GOOGLE_SCHOLAR_ID']
    os.makedirs(RESULTS_DIR, exist_ok=True)

    try:
        author = fetch_author(scholar_id)
    except Exception as e:  # noqa: BLE001 - any failure should fall back
        if os.path.exists(DATA_FILE):
            print(f'WARNING: fetching citation data failed ({e!r}); '
                  'keeping previous results', file=sys.stderr)
            return
        raise

    author['publications'] = {v['author_pub_id']: v for v in author['publications']}
    # Round-trip through JSON first: in-memory objects can contain tuples
    # or other types that never compare equal to their loaded counterparts.
    author = json.loads(json.dumps(author, ensure_ascii=False))

    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, encoding='utf-8') as f:
            old = json.load(f)
        old.pop('updated', None)
        if old == author:
            print('Citation data unchanged; not rewriting files')
            return

    author['updated'] = str(datetime.now())
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(author, f, ensure_ascii=False)

    shieldio_data = {
        'schemaVersion': 1,
        'label': 'citations',
        'message': f"{author['citedby']}",
    }
    with open(SHIELDS_FILE, 'w', encoding='utf-8') as f:
        json.dump(shieldio_data, f, ensure_ascii=False)

    print(f"Updated citation data for {author['name']}: "
          f"citedby={author['citedby']}, hindex={author['hindex']}, "
          f"i10index={author['i10index']}, "
          f"publications={len(author['publications'])}")


if __name__ == '__main__':
    main()
