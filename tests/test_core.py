from modelscope import select_by_family


def test_select_by_family():
    models = [{"name": "a", "family": "Llama"}, {"name": "b", "family": "Gemma"}]
    assert select_by_family(models, "llama") == [models[0]]
