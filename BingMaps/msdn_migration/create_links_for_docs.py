import yaml, pandas
data = None
with open('link_mappings.yml', 'r') as f:
    data = yaml.load(f)

new_data = {'msdn': [], 'review':[], 'final': []}

review_endpoint = "https://review.docs.microsoft.com/en-us/bingmaps"
final_endpoint = "https://docs.microsoft.com/en-us/bingmaps"

for datum in data:
    path = datum['path']
    for d in datum['links']:
        
        parts = d['new-docs'].split('/')

        if 'index.md' in parts[-1]:
            parts.pop()

        if parts:
            parts[-1] = parts[-1].replace('.md', '')
        
        html = '/'.join(parts)

        review_link = f"{review_endpoint}/{path}/{html}/?branch=master"
        final_link = f"{final_endpoint}/{path}/{html}"
        msdn = d['msdn']

        new_data['msdn'].append(msdn)
        new_data['review'].append(review_link)
        new_data['final'].append(final_link)


df = pandas.DataFrame.from_dict(new_data)
df.to_excel('bing_maps_redirections.xlsx')