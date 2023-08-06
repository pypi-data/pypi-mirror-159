from pharmpy.tools.amd.funcs import create_start_model


def test_create_start_model(testdata):
    path = testdata / 'nonmem' / 'pheno.dta'
    model = create_start_model(path, modeltype='pk_iv')
    sep = model.datainfo.separator
    assert sep == "\\s+"
    assert len(model.dataset.columns) == 6
    assert len(model.parameters) == 6
    assert 'POP_CL' in model.parameters
    assert 'POP_MAT' not in model.parameters

    model = create_start_model(path, modeltype='pk_oral')
    assert 'POP_CL' in model.parameters
    assert 'POP_MAT' in model.parameters
