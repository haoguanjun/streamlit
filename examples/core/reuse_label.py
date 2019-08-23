# -*- coding: utf-8 -*-
# Copyright 2018-2019 Streamlit Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st

if not hasattr(st, 'test_run_count'):
    st.test_run_count = 0
else:
    st.test_run_count += 1

# Starting the report takes up the first run.
# When run the test will see the slider first.
if not st.test_run_count:
    w1 = st.button('label')
elif st.test_run_count == 1:
    w1 = st.slider('label', 25, 0, 100, 1)
else:
    w1 = st.selectbox('label', ('m', 'f'), 1)

st.write('value 1:', w1)