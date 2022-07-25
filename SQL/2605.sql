SELECT pd.name, pv.name
FROM products pd, providers pv, categories c
WHERE pd.id_providers = pv.id
  AND c.id = pd.id_categories
  AND c.id = 6;
