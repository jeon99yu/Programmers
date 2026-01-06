SELECT T1.item_id, item_name, rarity
FROM item_info T1
JOIN item_tree T2
ON T1.item_id = T2.item_id
WHERE NOT EXISTS (  
    SELECT 1
    FROM item_tree
    WHERE parent_item_id = T1.item_id   
)
ORDER BY T1.item_id DESC