from tests.data.fields_metadata import geolayer_data_fields_metadata_complete

metadata_fr_dept_data_and_geometry = {
        "name": "FRANCE_DPT_GENERALIZE_LAMB93_ROUND_DATA_AND_GEOMETRY",
        "fields": geolayer_data_fields_metadata_complete,
        "geometry_ref": {"type": {"MultiPolygon", "Polygon"}, "crs": 2154},
    }

metadata_paris_velib = {
        "name": "geolayer_paris_velib",
        "fields": {
            "Identifiant station": {"type": "Integer", "index": 0},
            "Nom station": {"type": "String", "width": 45, "index": 1},
            "Station en fonctionnement": {"type": "String", "width": 3, "index": 2},
            "Capacité de la station": {"type": "Integer", "index": 3},
            "Nombre bornettes libres": {"type": "Integer", "index": 4},
            "Nombre total vélos disponibles": {"type": "Integer", "index": 5},
            "Vélos mécaniques disponibles": {"type": "Integer", "index": 6},
            "Vélos électriques disponibles": {"type": "Integer", "index": 7},
            "Borne de paiement disponible": {"type": "String", "width": 3, "index": 8},
            "Retour vélib possible": {"type": "String", "width": 3, "index": 9},
            "Actualisation de la donnée": {"type": "DateTime", "index": 10},
            "Coordonnées géographiques": {
                "type": "RealList",
                "width": 13,
                "precision": 11,
                "index": 11,
            },
            "Nom communes équipées": {"type": "String", "width": 20, "index": 12},
        },
    }