# ~~SourcePokeapi~~

> :warning: **DEPRECATED**: Typed connector configuration models are deprecated and will be removed in v1.1.0. Pass configuration as a plain dict with a required 'sourceType' key instead..


## Fields

| Field                                                                     | Type                                                                      | Required                                                                  | Description                                                               | Example                                                                   |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `pokemon_name`                                                            | [models.PokemonName](../models/pokemonname.md)                            | :heavy_check_mark:                                                        | Pokemon requested from the API.                                           | **Example 1:** ditto<br/>**Example 2:** luxray<br/>**Example 3:** snorlax |
| `source_type`                                                             | [models.Pokeapi](../models/pokeapi.md)                                    | :heavy_check_mark:                                                        | N/A                                                                       |                                                                           |