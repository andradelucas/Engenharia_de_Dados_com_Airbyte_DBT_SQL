SELECT   
    cliente_id,  
    nome, 
    cidade,  
    estado
  FROM {{ ref('clientes') }} c
WHERE c.estado IN ('SP','RJ','MG','ES')