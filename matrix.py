#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

classdict={'mathematics': ['linear algebra',
           'topology',
           'algebra',
           'calculus',
           'variational calculus',
           'functional field',
           'real analysis',
           'complex analysis',
           'differential equation',
           'statistics',
           'statistical optimization',
           'probability',
           'stochastic calculus',
           'numerical analysis',
           'differential geometry'],
          'physics': ['renormalization',
           'classical mechanics',
           'quantum mechanics',
           'statistical mechanics',
           'functional field',
           'path integral',
           'quantum field theory',
           'electrodynamics',
           'condensed matter',
           'particle physics',
           'topological solitons',
           'astrophysics',
           'spontaneous symmetry breaking',
           'atomic molecular and optical physics',
           'quantum chaos'],
          'theology': ['divine providence',
           'soteriology',
           'anthropology',
           'pneumatology',
           'Christology',
           'Holy Trinity',
           'eschatology',
           'scripture',
           'ecclesiology',
           'predestination',
           'divine degree',
           'creedal confessionalism',
           'scholasticism',
           'prayer',
           'Eucharist']}


orderedNames = ['mathematics','physics','theology']

dataMatrix = np.array([classdict[i] for i in orderedNames])

print (dataMatrix)