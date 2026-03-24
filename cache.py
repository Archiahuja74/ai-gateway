cache = {}

def get_from_cache(prompt):
    return cache.get(prompt)

def save_to_cache(prompt, response):
    cache[prompt] = response