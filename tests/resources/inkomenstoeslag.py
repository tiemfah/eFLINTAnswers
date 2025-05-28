INCOME_SUPPLEMENT_TYPES = {
    'types': {
        '[AOW leeftijd behaald]': {
            'closed': True,
            'conditions': [],
            'derivation': [],
            'domain': {
                'domain-type': 'Products',
                'vars': []
            },
            'domain_constraint': {
                'b': True,
                'term-type': 'BoolLit'
            },
            'kind': {
                'fact': {
                    'actor': False,
                    'invariant': False
                },
                'kind-type': 'Fact'
            }
        },
        '[Aanvrager woonachtig in Utrecht]': {
            'closed': True,
            'conditions': [],
            'derivation': [
                {
                    'derivation-type': 'HoldsWhen',
                    'term': {
                        't': {
                            'domID': '[Woonplaats]',
                            't': {
                                'string': 'Utrecht',
                                'term-type': 'StringLit'
                            },
                            'term-type': 'Tag'
                        },
                        'term-type': 'Present'
                    }
                }
            ],
            'domain': {
                'domain-type': 'Products',
                'vars': []
            },
            'domain_constraint': {
                'b': True,
                'term-type': 'BoolLit'
            },
            'kind': {
                'fact': {
                    'actor': False,
                    'invariant': False
                },
                'kind-type': 'Fact'
            }
        },
        '[Alleenstaande]': {
            'closed': True,
            'conditions': [],
            'derivation': [],
            'domain': {
                'domain-type': 'Products',
                'vars': []
            },
            'domain_constraint': {
                'b': True,
                'term-type': 'BoolLit'
            },
            'kind': {
                'fact': {
                    'actor': False,
                    'invariant': False
                },
                'kind-type': 'Fact'
            }
        },
        '[BOVENGRENS_INKOMEN_ALLEENSTAANDE]': {
            'closed': True,
            'conditions': [],
            'derivation': [],
            'domain': {
                'domain-type': 'AnyInt'
            },
            'domain_constraint': {
                'b': True,
                'term-type': 'BoolLit'
            },
            'kind': {
                'fact': {
                    'actor': False,
                    'invariant': False
                },
                'kind-type': 'Fact'
            }
        },
        '[BOVENGRENS_INKOMEN_NIET_ALLEENSTAANDE]': {
            'closed': True,
            'conditions': [],
            'derivation': [],
            'domain': {
                'domain-type': 'AnyInt'
            },
            'domain_constraint': {
                'b': True,
                'term-type': 'BoolLit'
            },
            'kind': {
                'fact': {
                    'actor': False,
                    'invariant': False
                },
                'kind-type': 'Fact'
            }
        },
        '[BOVENGRENS_VERMOGEN_HOOG]': {
            'closed': True,
            'conditions': [],
            'derivation': [],
            'domain': {
                'domain-type': 'AnyInt'
            },
            'domain_constraint': {
                'b': True,
                'term-type': 'BoolLit'
            },
            'kind': {
                'fact': {
                    'actor': False,
                    'invariant': False
                },
                'kind-type': 'Fact'
            }
        },
        '[BOVENGRENS_VERMOGEN_LAAG]': {
            'closed': True,
            'conditions': [],
            'derivation': [],
            'domain': {
                'domain-type': 'AnyInt'
            },
            'domain_constraint': {
                'b': True,
                'term-type': 'BoolLit'
            },
            'kind': {
                'fact': {
                    'actor': False,
                    'invariant': False
                },
                'kind-type': 'Fact'
            }
        },
        '[Inkomen per maand]': {
            'closed': True,
            'conditions': [],
            'derivation': [],
            'domain': {
                'domain-type': 'AnyInt'
            },
            'domain_constraint': {
                'b': True,
                'term-type': 'BoolLit'
            },
            'kind': {
                'fact': {
                    'actor': False,
                    'invariant': False
                },
                'kind-type': 'Fact'
            }
        },
        '[Ouder dan 21]': {
            'closed': True,
            'conditions': [],
            'derivation': [],
            'domain': {
                'domain-type': 'Products',
                'vars': []
            },
            'domain_constraint': {
                'b': True,
                'term-type': 'BoolLit'
            },
            'kind': {
                'fact': {
                    'actor': False,
                    'invariant': False
                },
                'kind-type': 'Fact'
            }
        },
        '[Recht beschrijving]': {
            'closed': True,
            'conditions': [],
            'derivation': [
                {
                    'derivation-type': 'Dv',
                    'term': {
                        't1': {
                            'domID': '[Recht beschrijving]',
                            't': {
                                'string': 'Recht op IIT €591',
                                'term-type': 'StringLit'
                            },
                            'term-type': 'Tag'
                        },
                        't2': {
                            't': {
                                'term-type': 'Ref',
                                'var': {
                                    'domID': '[Recht op IIT 591]',
                                    'string': ''
                                }
                            },
                            'term-type': 'Present'
                        },
                        'term-type': 'When'
                    },
                    'vars': [
                        {
                            'domID': '[Recht op IIT 591]',
                            'string': ''
                        }
                    ]
                },
                {
                    'derivation-type': 'Dv',
                    'term': {
                        't1': {
                            'domID': '[Recht beschrijving]',
                            't': {
                                'string': 'Recht op IIT €231',
                                'term-type': 'StringLit'
                            },
                            'term-type': 'Tag'
                        },
                        't2': {
                            't': {
                                'term-type': 'Ref',
                                'var': {
                                    'domID': '[Recht op IIT 231]',
                                    'string': ''
                                }
                            },
                            'term-type': 'Present'
                        },
                        'term-type': 'When'
                    },
                    'vars': [
                        {
                            'domID': '[Recht op IIT 231]',
                            'string': ''
                        }
                    ]
                },
                {
                    'derivation-type': 'Dv',
                    'term': {
                        't1': {
                            'domID': '[Recht beschrijving]',
                            't': {
                                'string': 'Recht op IIT €51',
                                'term-type': 'StringLit'
                            },
                            'term-type': 'Tag'
                        },
                        't2': {
                            't': {
                                'term-type': 'Ref',
                                'var': {
                                    'domID': '[Recht op IIT 51]',
                                    'string': ''
                                }
                            },
                            'term-type': 'Present'
                        },
                        'term-type': 'When'
                    },
                    'vars': [
                        {
                            'domID': '[Recht op IIT 51]',
                            'string': ''
                        }
                    ]
                }
            ],
            'domain': {
                'domain-type': 'AnyString'
            },
            'domain_constraint': {
                'b': True,
                'term-type': 'BoolLit'
            },
            'kind': {
                'fact': {
                    'actor': False,
                    'invariant': False
                },
                'kind-type': 'Fact'
            }
        },
        '[Recht op IIT 231]': {
            'closed': True,
            'conditions': [],
            'derivation': [
                {
                    'derivation-type': 'HoldsWhen',
                    'term': {
                        't': {
                            't1': {
                                't': {
                                    'term-type': 'Ref',
                                    'var': {
                                        'domID': '[Aanvrager woonachtig in Utrecht]',
                                        'string': ''
                                    }
                                },
                                'term-type': 'Present'
                            },
                            't2': {
                                't1': {
                                    't': {
                                        't': {
                                            'term-type': 'Ref',
                                            'var': {
                                                'domID': '[AOW leeftijd behaald]',
                                                'string': ''
                                            }
                                        },
                                        'term-type': 'Present'
                                    },
                                    'term-type': 'Not'
                                },
                                't2': {
                                    't1': {
                                        't': {
                                            'term-type': 'Ref',
                                            'var': {
                                                'domID': '[Ouder dan 21]',
                                                'string': ''
                                            }
                                        },
                                        'term-type': 'Present'
                                    },
                                    't2': {
                                        't1': {
                                            't': {
                                                'term-type': 'Ref',
                                                'var': {
                                                    'domID': '[Alleenstaande]',
                                                    'string': ''
                                                }
                                            },
                                            'term-type': 'Present'
                                        },
                                        't2': {
                                            't1': {
                                                't': {
                                                    't': {
                                                        'term-type': 'Ref',
                                                        'var': {
                                                            'domID': '[Thuiswonende kinderen]',
                                                            'string': ''
                                                        }
                                                    },
                                                    'term-type': 'Present'
                                                },
                                                'term-type': 'Not'
                                            },
                                            't2': {
                                                't1': {
                                                    't1': {
                                                        't': {
                                                            'term-type': 'Ref',
                                                            'var': {
                                                                'domID': '[Inkomen per maand]',
                                                                'string': ''
                                                            }
                                                        },
                                                        'term-type': 'Untag'
                                                    },
                                                    't2': {
                                                        't': {
                                                            'term-type': 'Ref',
                                                            'var': {
                                                                'domID': '[BOVENGRENS_INKOMEN_ALLEENSTAANDE]',
                                                                'string': ''
                                                            }
                                                        },
                                                        'term-type': 'Untag'
                                                    },
                                                    'term-type': 'Leq'
                                                },
                                                't2': {
                                                    't1': {
                                                        't': {
                                                            'term-type': 'Ref',
                                                            'var': {
                                                                'domID': '[Vermogen]',
                                                                'string': ''
                                                            }
                                                        },
                                                        'term-type': 'Untag'
                                                    },
                                                    't2': {
                                                        't': {
                                                            'term-type': 'Ref',
                                                            'var': {
                                                                'domID': '[BOVENGRENS_VERMOGEN_LAAG]',
                                                                'string': ''
                                                            }
                                                        },
                                                        'term-type': 'Untag'
                                                    },
                                                    'term-type': 'Leq'
                                                },
                                                'term-type': 'And'
                                            },
                                            'term-type': 'And'
                                        },
                                        'term-type': 'And'
                                    },
                                    'term-type': 'And'
                                },
                                'term-type': 'And'
                            },
                            'term-type': 'And'
                        },
                        'term-type': 'Exists',
                        'vars': [
                            {
                                'domID': '[AOW leeftijd behaald]',
                                'string': ''
                            },
                            {
                                'domID': '[Aanvrager woonachtig in Utrecht]',
                                'string': ''
                            },
                            {
                                'domID': '[Alleenstaande]',
                                'string': ''
                            },
                            {
                                'domID': '[BOVENGRENS_INKOMEN_ALLEENSTAANDE]',
                                'string': ''
                            },
                            {
                                'domID': '[BOVENGRENS_VERMOGEN_LAAG]',
                                'string': ''
                            },
                            {
                                'domID': '[Inkomen per maand]',
                                'string': ''
                            },
                            {
                                'domID': '[Ouder dan 21]',
                                'string': ''
                            },
                            {
                                'domID': '[Thuiswonende kinderen]',
                                'string': ''
                            },
                            {
                                'domID': '[Vermogen]',
                                'string': ''
                            }
                        ]
                    }
                }
            ],
            'domain': {
                'domain-type': 'Products',
                'vars': []
            },
            'domain_constraint': {
                'b': True,
                'term-type': 'BoolLit'
            },
            'kind': {
                'fact': {
                    'actor': False,
                    'invariant': False
                },
                'kind-type': 'Fact'
            }
        },
        '[Recht op IIT 51]': {
            'closed': True,
            'conditions': [],
            'derivation': [
                {
                    'derivation-type': 'HoldsWhen',
                    'term': {
                        't': {
                            't1': {
                                't': {
                                    'term-type': 'Ref',
                                    'var': {
                                        'domID': '[Aanvrager woonachtig in Utrecht]',
                                        'string': ''
                                    }
                                },
                                'term-type': 'Present'
                            },
                            't2': {
                                't1': {
                                    't': {
                                        't': {
                                            'term-type': 'Ref',
                                            'var': {
                                                'domID': '[AOW leeftijd behaald]',
                                                'string': ''
                                            }
                                        },
                                        'term-type': 'Present'
                                    },
                                    'term-type': 'Not'
                                },
                                't2': {
                                    't1': {
                                        't': {
                                            'term-type': 'Ref',
                                            'var': {
                                                'domID': '[Ouder dan 21]',
                                                'string': ''
                                            }
                                        },
                                        'term-type': 'Present'
                                    },
                                    't2': {
                                        't1': {
                                            't': {
                                                'term-type': 'Ref',
                                                'var': {
                                                    'domID': '[Alleenstaande]',
                                                    'string': ''
                                                }
                                            },
                                            'term-type': 'Present'
                                        },
                                        't2': {
                                            't1': {
                                                't': {
                                                    'term-type': 'Ref',
                                                    'var': {
                                                        'domID': '[Thuiswonende kinderen]',
                                                        'string': ''
                                                    }
                                                },
                                                'term-type': 'Present'
                                            },
                                            't2': {
                                                't1': {
                                                    't1': {
                                                        't': {
                                                            'term-type': 'Ref',
                                                            'var': {
                                                                'domID': '[Inkomen per maand]',
                                                                'string': ''
                                                            }
                                                        },
                                                        'term-type': 'Untag'
                                                    },
                                                    't2': {
                                                        't': {
                                                            'term-type': 'Ref',
                                                            'var': {
                                                                'domID': '[BOVENGRENS_INKOMEN_ALLEENSTAANDE]',
                                                                'string': ''
                                                            }
                                                        },
                                                        'term-type': 'Untag'
                                                    },
                                                    'term-type': 'Leq'
                                                },
                                                't2': {
                                                    't1': {
                                                        't': {
                                                            'term-type': 'Ref',
                                                            'var': {
                                                                'domID': '[Vermogen]',
                                                                'string': ''
                                                            }
                                                        },
                                                        'term-type': 'Untag'
                                                    },
                                                    't2': {
                                                        't': {
                                                            'term-type': 'Ref',
                                                            'var': {
                                                                'domID': '[BOVENGRENS_VERMOGEN_HOOG]',
                                                                'string': ''
                                                            }
                                                        },
                                                        'term-type': 'Untag'
                                                    },
                                                    'term-type': 'Leq'
                                                },
                                                'term-type': 'And'
                                            },
                                            'term-type': 'And'
                                        },
                                        'term-type': 'And'
                                    },
                                    'term-type': 'And'
                                },
                                'term-type': 'And'
                            },
                            'term-type': 'And'
                        },
                        'term-type': 'Exists',
                        'vars': [
                            {
                                'domID': '[AOW leeftijd behaald]',
                                'string': ''
                            },
                            {
                                'domID': '[Aanvrager woonachtig in Utrecht]',
                                'string': ''
                            },
                            {
                                'domID': '[Alleenstaande]',
                                'string': ''
                            },
                            {
                                'domID': '[BOVENGRENS_INKOMEN_ALLEENSTAANDE]',
                                'string': ''
                            },
                            {
                                'domID': '[BOVENGRENS_VERMOGEN_HOOG]',
                                'string': ''
                            },
                            {
                                'domID': '[Inkomen per maand]',
                                'string': ''
                            },
                            {
                                'domID': '[Ouder dan 21]',
                                'string': ''
                            },
                            {
                                'domID': '[Thuiswonende kinderen]',
                                'string': ''
                            },
                            {
                                'domID': '[Vermogen]',
                                'string': ''
                            }
                        ]
                    }
                }
            ],
            'domain': {
                'domain-type': 'Products',
                'vars': []
            },
            'domain_constraint': {
                'b': True,
                'term-type': 'BoolLit'
            },
            'kind': {
                'fact': {
                    'actor': False,
                    'invariant': False
                },
                'kind-type': 'Fact'
            }
        },
        '[Recht op IIT 591]': {
            'closed': True,
            'conditions': [],
            'derivation': [
                {
                    'derivation-type': 'HoldsWhen',
                    'term': {
                        't': {
                            't1': {
                                't': {
                                    'term-type': 'Ref',
                                    'var': {
                                        'domID': '[Aanvrager woonachtig in Utrecht]',
                                        'string': ''
                                    }
                                },
                                'term-type': 'Present'
                            },
                            't2': {
                                't1': {
                                    't': {
                                        't': {
                                            'term-type': 'Ref',
                                            'var': {
                                                'domID': '[AOW leeftijd behaald]',
                                                'string': ''
                                            }
                                        },
                                        'term-type': 'Present'
                                    },
                                    'term-type': 'Not'
                                },
                                't2': {
                                    't1': {
                                        't': {
                                            'term-type': 'Ref',
                                            'var': {
                                                'domID': '[Ouder dan 21]',
                                                'string': ''
                                            }
                                        },
                                        'term-type': 'Present'
                                    },
                                    't2': {
                                        't1': {
                                            't': {
                                                't': {
                                                    'term-type': 'Ref',
                                                    'var': {
                                                        'domID': '[Alleenstaande]',
                                                        'string': ''
                                                    }
                                                },
                                                'term-type': 'Present'
                                            },
                                            'term-type': 'Not'
                                        },
                                        't2': {
                                            't1': {
                                                't1': {
                                                    't': {
                                                        'term-type': 'Ref',
                                                        'var': {
                                                            'domID': '[Inkomen per maand]',
                                                            'string': ''
                                                        }
                                                    },
                                                    'term-type': 'Untag'
                                                },
                                                't2': {
                                                    't': {
                                                        'term-type': 'Ref',
                                                        'var': {
                                                            'domID': '[BOVENGRENS_INKOMEN_NIET_ALLEENSTAANDE]',
                                                            'string': ''
                                                        }
                                                    },
                                                    'term-type': 'Untag'
                                                },
                                                'term-type': 'Leq'
                                            },
                                            't2': {
                                                't1': {
                                                    't': {
                                                        'term-type': 'Ref',
                                                        'var': {
                                                            'domID': '[Vermogen]',
                                                            'string': ''
                                                        }
                                                    },
                                                    'term-type': 'Untag'
                                                },
                                                't2': {
                                                    't': {
                                                        'term-type': 'Ref',
                                                        'var': {
                                                            'domID': '[BOVENGRENS_VERMOGEN_HOOG]',
                                                            'string': ''
                                                        }
                                                    },
                                                    'term-type': 'Untag'
                                                },
                                                'term-type': 'Leq'
                                            },
                                            'term-type': 'And'
                                        },
                                        'term-type': 'And'
                                    },
                                    'term-type': 'And'
                                },
                                'term-type': 'And'
                            },
                            'term-type': 'And'
                        },
                        'term-type': 'Exists',
                        'vars': [
                            {
                                'domID': '[AOW leeftijd behaald]',
                                'string': ''
                            },
                            {
                                'domID': '[Aanvrager woonachtig in Utrecht]',
                                'string': ''
                            },
                            {
                                'domID': '[Alleenstaande]',
                                'string': ''
                            },
                            {
                                'domID': '[BOVENGRENS_INKOMEN_NIET_ALLEENSTAANDE]',
                                'string': ''
                            },
                            {
                                'domID': '[BOVENGRENS_VERMOGEN_HOOG]',
                                'string': ''
                            },
                            {
                                'domID': '[Inkomen per maand]',
                                'string': ''
                            },
                            {
                                'domID': '[Ouder dan 21]',
                                'string': ''
                            },
                            {
                                'domID': '[Vermogen]',
                                'string': ''
                            }
                        ]
                    }
                }
            ],
            'domain': {
                'domain-type': 'Products',
                'vars': []
            },
            'domain_constraint': {
                'b': True,
                'term-type': 'BoolLit'
            },
            'kind': {
                'fact': {
                    'actor': False,
                    'invariant': False
                },
                'kind-type': 'Fact'
            }
        },
        '[Thuiswonende kinderen]': {
            'closed': True,
            'conditions': [],
            'derivation': [],
            'domain': {
                'domain-type': 'Products',
                'vars': []
            },
            'domain_constraint': {
                'b': True,
                'term-type': 'BoolLit'
            },
            'kind': {
                'fact': {
                    'actor': False,
                    'invariant': False
                },
                'kind-type': 'Fact'
            }
        },
        '[Uit te keren individuele inkomenstoeslag]': {
            'closed': True,
            'conditions': [],
            'derivation': [
                {
                    'derivation-type': 'Dv',
                    'term': {
                        't1': {
                            'domID': '[Uit te keren individuele inkomenstoeslag]',
                            't': {
                                'int': 591,
                                'term-type': 'IntLit'
                            },
                            'term-type': 'Tag'
                        },
                        't2': {
                            't': {
                                'term-type': 'Ref',
                                'var': {
                                    'domID': '[Recht op IIT 591]',
                                    'string': ''
                                }
                            },
                            'term-type': 'Present'
                        },
                        'term-type': 'When'
                    },
                    'vars': [
                        {
                            'domID': '[Recht op IIT 591]',
                            'string': ''
                        }
                    ]
                },
                {
                    'derivation-type': 'Dv',
                    'term': {
                        't1': {
                            'domID': '[Uit te keren individuele inkomenstoeslag]',
                            't': {
                                'int': 231,
                                'term-type': 'IntLit'
                            },
                            'term-type': 'Tag'
                        },
                        't2': {
                            't': {
                                'term-type': 'Ref',
                                'var': {
                                    'domID': '[Recht op IIT 231]',
                                    'string': ''
                                }
                            },
                            'term-type': 'Present'
                        },
                        'term-type': 'When'
                    },
                    'vars': [
                        {
                            'domID': '[Recht op IIT 231]',
                            'string': ''
                        }
                    ]
                },
                {
                    'derivation-type': 'Dv',
                    'term': {
                        't1': {
                            'domID': '[Uit te keren individuele inkomenstoeslag]',
                            't': {
                                'int': 51,
                                'term-type': 'IntLit'
                            },
                            'term-type': 'Tag'
                        },
                        't2': {
                            't': {
                                'term-type': 'Ref',
                                'var': {
                                    'domID': '[Recht op IIT 51]',
                                    'string': ''
                                }
                            },
                            'term-type': 'Present'
                        },
                        'term-type': 'When'
                    },
                    'vars': [
                        {
                            'domID': '[Recht op IIT 51]',
                            'string': ''
                        }
                    ]
                }
            ],
            'domain': {
                'domain-type': 'AnyInt'
            },
            'domain_constraint': {
                'b': True,
                'term-type': 'BoolLit'
            },
            'kind': {
                'fact': {
                    'actor': False,
                    'invariant': False
                },
                'kind-type': 'Fact'
            }
        },
        '[Vermogen]': {
            'closed': True,
            'conditions': [],
            'derivation': [],
            'domain': {
                'domain-type': 'AnyInt'
            },
            'domain_constraint': {
                'b': True,
                'term-type': 'BoolLit'
            },
            'kind': {
                'fact': {
                    'actor': False,
                    'invariant': False
                },
                'kind-type': 'Fact'
            }
        },
        '[Woonplaats]': {
            'closed': True,
            'conditions': [],
            'derivation': [],
            'domain': {
                'domain-type': 'AnyString'
            },
            'domain_constraint': {
                'b': True,
                'term-type': 'BoolLit'
            },
            'kind': {
                'fact': {
                    'actor': False,
                    'invariant': False
                },
                'kind-type': 'Fact'
            }
        },
        'actor': {
            'closed': True,
            'conditions': [],
            'derivation': [],
            'domain': {
                'domain-type': 'AnyString'
            },
            'domain_constraint': {
                'b': True,
                'term-type': 'BoolLit'
            },
            'kind': {
                'fact': {
                    'actor': True,
                    'invariant': False
                },
                'kind-type': 'Fact'
            }
        },
        'int': {
            'closed': True,
            'conditions': [],
            'derivation': [],
            'domain': {
                'domain-type': 'AnyInt'
            },
            'domain_constraint': {
                'b': True,
                'term-type': 'BoolLit'
            },
            'kind': {
                'fact': {
                    'actor': False,
                    'invariant': False
                },
                'kind-type': 'Fact'
            }
        },
        'string': {
            'closed': True,
            'conditions': [],
            'derivation': [],
            'domain': {
                'domain-type': 'AnyString'
            },
            'domain_constraint': {
                'b': True,
                'term-type': 'BoolLit'
            },
            'kind': {
                'fact': {
                    'actor': False,
                    'invariant': False
                },
                'kind-type': 'Fact'
            }
        }
    }
}
