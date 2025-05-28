HUMAN_EFLINT_TYPES = {
    'types': {
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
        'biped': {
            'closed': True,
            'conditions': [],
            'derivation': [
                {
                    'derivation-type': 'HoldsWhen',
                    'term': {
                        't': {
                            't': {
                                'args': {
                                    'Right': [
                                        {
                                            'term': {
                                                'term-type': 'Ref',
                                                'var': {
                                                    'domID': 'entity',
                                                    'string': ''
                                                }
                                            },
                                            'var': {
                                                'domID': 'entity',
                                                'string': ''
                                            }
                                        },
                                        {
                                            'term': {
                                                'domID': 'int',
                                                't': {
                                                    'int': 2,
                                                    'term-type': 'IntLit'
                                                },
                                                'term-type': 'Tag'
                                            },
                                            'var': {
                                                'domID': 'int',
                                                'string': ''
                                            }
                                        }
                                    ]
                                },
                                'domID': 'number_of_legs',
                                'term-type': 'App'
                            },
                            'term-type': 'Present'
                        },
                        'term-type': 'Exists',
                        'vars': [
                            {
                                'domID': 'number_of_legs',
                                'string': ''
                            }
                        ]
                    }
                }
            ],
            'domain': {
                'domain-type': 'Products',
                'vars': [
                    {
                        'domID': 'entity',
                        'string': ''
                    }
                ]
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
        'entity': {
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
        'featherless': {
            'closed': True,
            'conditions': [],
            'derivation': [],
            'domain': {
                'domain-type': 'Products',
                'vars': [
                    {
                        'domID': 'entity',
                        'string': ''
                    }
                ]
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
        'human': {
            'closed': True,
            'conditions': [],
            'derivation': [
                {
                    'derivation-type': 'HoldsWhen',
                    'term': {
                        't1': {
                            't1': {
                                't': {
                                    'args': {
                                        'Right': [
                                            {
                                                'term': {
                                                    'term-type': 'Ref',
                                                    'var': {
                                                        'domID': 'entity',
                                                        'string': ''
                                                    }
                                                },
                                                'var': {
                                                    'domID': 'entity',
                                                    'string': ''
                                                }
                                            }
                                        ]
                                    },
                                    'domID': 'biped',
                                    'term-type': 'App'
                                },
                                'term-type': 'Present'
                            },
                            't2': {
                                't': {
                                    'args': {
                                        'Right': [
                                            {
                                                'term': {
                                                    'term-type': 'Ref',
                                                    'var': {
                                                        'domID': 'entity',
                                                        'string': ''
                                                    }
                                                },
                                                'var': {
                                                    'domID': 'entity',
                                                    'string': ''
                                                }
                                            }
                                        ]
                                    },
                                    'domID': 'featherless',
                                    'term-type': 'App'
                                },
                                'term-type': 'Present'
                            },
                            'term-type': 'And'
                        },
                        't2': {
                            't': {
                                'args': {
                                    'Right': [
                                        {
                                            'term': {
                                                'term-type': 'Ref',
                                                'var': {
                                                    'domID': 'entity',
                                                    'string': ''
                                                }
                                            },
                                            'var': {
                                                'domID': 'entity',
                                                'string': ''
                                            }
                                        }
                                    ]
                                },
                                'domID': 'intelligent',
                                'term-type': 'App'
                            },
                            'term-type': 'Present'
                        },
                        'term-type': 'Or'
                    }
                }
            ],
            'domain': {
                'domain-type': 'Products',
                'vars': [
                    {
                        'domID': 'entity',
                        'string': ''
                    }
                ]
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
        'intelligent': {
            'closed': True,
            'conditions': [],
            'derivation': [],
            'domain': {
                'domain-type': 'Products',
                'vars': [
                    {
                        'domID': 'entity',
                        'string': ''
                    }
                ]
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
        'number_of_legs': {
            'closed': True,
            'conditions': [],
            'derivation': [],
            'domain': {
                'domain-type': 'Products',
                'vars': [
                    {
                        'domID': 'entity',
                        'string': ''
                    },
                    {
                        'domID': 'int',
                        'string': ''
                    }
                ]
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
