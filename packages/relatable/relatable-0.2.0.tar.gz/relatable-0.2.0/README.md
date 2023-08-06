# relatable

relatable is a Python package for converting a collection of documents, 
such as a MongoDB collection, into an interrelated set of tables, such as a 
schema in a relational database.

## Installation

```
pip3 install relatable
```

## Example of use

Consider the following list of dictionaries:

```
docs = [
  {
    "name": "Alice",
    "age": 34,
    "experience": [
      {
        "company": "Google",
        "role": "Software Engineer",
        "from": 2020,
        "to": 2022,
        "responsibilities": [
          "Google stuff",
          "Mark TensorFlow issues as \"Won't Do\""
        ],
        "technologies": [
          "C++",
          "LolCode"
        ]
      },
      {
        "company": "Facebook",
        "role": "Senior Data Scientist",
        "from": 2017,
        "to": 2020,
        "responsibilities": [
          "Censor media",
          "Learn the foundations of ML",
          "Do Kaggle competitions"
        ],
        "technologies": [
          "Python",
          "Excel"
        ]
      }
    ]
  },
  {
    "name": "Bob",
    "age": 27,
    "experience": [
      {
        "company": "OpenAI",
        "role": "NLP Engineer",
        "from": 2019,
        "to": 2022,
        "responsibilities": [
          "Assert that GPT-2 is racist",
          "Assert that GPT-3 is racist",
          "Develop a prototype of a premium non-racist language model"
        ],
        "technologies": [
          "Triton",
          "LaTeX"
        ]
      }
    ]
  }
]
```

To generate a relational schema for the above data, let's instantiate a `RelationalSchema` with `docs` as input:

```
from relatable import RelationalSchema

rs = RelationalSchema(docs)
```

Once the RelationalSchema is instantiated, we can check its metadata. This metadata is a list of flat dictionaries, so 
we can make use of Pandas to load it into a DataFrame:

```
import pandas as pd

pd.DataFrame(rs.generate_metadata())
```

|     | table | field                       | type    | nullable | unique |
|----:|:------|:----------------------------|:--------|:---------|:-------|
|   0 | t0    | t0_id                       | Integer | False    | True   |
|   1 | t0    | name                        | String  | False    | True   |
|   2 | t0    | age                         | Integer | False    | True   |
|   3 | t1    | t1_id                       | Integer | False    | True   |
|   4 | t1    | t0_id                       | Integer | False    | False  |
|   5 | t1    | experience.company          | String  | False    | True   |
|   6 | t1    | experience.role             | String  | False    | True   |
|   7 | t1    | experience.from             | Integer | False    | True   |
|   8 | t1    | experience.to               | Integer | False    | False  |
|   9 | t2    | t2_id                       | Integer | False    | True   |
|  10 | t2    | t1_id                       | Integer | False    | False  |
|  11 | t2    | t0_id                       | Integer | False    | False  |
|  12 | t2    | experience.technologies     | String  | False    | True   |
|  13 | t3    | t3_id                       | Integer | False    | True   |
|  14 | t3    | t1_id                       | Integer | False    | False  |
|  15 | t3    | t0_id                       | Integer | False    | False  |
|  16 | t3    | experience.responsibilities | String  | False    | True   | 

We can see that `RelationalSchema` has inferred a relational schema containing four tables with primary keys and 
foreign keys.

It would be nice to rename these tables with a more descriptive name, and also rename some columns. We can do so with 
the `rename` and `rename_column` methods:

```
rs.rename_table("t0", "person")
rs.rename_table("t1", "job")
rs.rename_table("t2", "technology")
rs.rename_table("t3", "responsibility")

for name in ["company", "role", "from", "to"]:
    rs.rename_column("job", f"experience.{name}", name)

rs.rename_column("technology", "experience.technologies", "technology")
rs.rename_column("responsibility", "experience.responsibilities", "responsibility")

pd.DataFrame(rs.generate_metadata())
```

|     | table          | field             | type    | nullable | unique |
|----:|:---------------|:------------------|:--------|:---------|:-------|
|   0 | person         | person_id         | Integer | False    | True   |
|   1 | person         | name              | String  | False    | True   |
|   2 | person         | age               | Integer | False    | True   |
|   3 | job            | job_id            | Integer | False    | True   |
|   4 | job            | person_id         | Integer | False    | False  |
|   5 | job            | company           | String  | False    | True   |
|   6 | job            | role              | String  | False    | True   |
|   7 | job            | from              | Integer | False    | True   |
|   8 | job            | to                | Integer | False    | False  |
|   9 | technology     | technology_id     | Integer | False    | True   |
|  10 | technology     | job_id            | Integer | False    | False  |
|  11 | technology     | person_id         | Integer | False    | False  |
|  12 | technology     | technology        | String  | False    | True   |
|  13 | responsibility | responsibility_id | Integer | False    | True   |
|  14 | responsibility | job_id            | Integer | False    | False  |
|  15 | responsibility | person_id         | Integer | False    | False  |
|  16 | responsibility | responsibility    | String  | False    | True   | 

Finally, let's look at each of the tables:

```
dfs = [pd.DataFrame(t.data).set_index(t.primary_key) for t in rs.tables]
```

Table person:

| person_id | name  | age |
|----------:|:------|----:|
|         0 | Alice |  34 |
|         1 | Bob   |  27 | 

Table job:

| job_id | person_id | company  | role                  | from |   to |
|-------:|----------:|:---------|:----------------------|-----:|-----:|
|      0 |         0 | Google   | Software Engineer     | 2020 | 2022 |
|      1 |         0 | Facebook | Senior Data Scientist | 2017 | 2020 |
|      2 |         1 | OpenAI   | NLP Engineer          | 2019 | 2022 | 

Table technology:

| technology_id | job_id | person_id | technology |
|--------------:|-------:|----------:|:-----------|
|             0 |      0 |         0 | C++        |
|             1 |      0 |         0 | LolCode    |
|             2 |      1 |         0 | Python     |
|             3 |      1 |         0 | Excel      |
|             4 |      2 |         1 | Triton     |
|             5 |      2 |         1 | LaTeX      | 

Table responsibility:

| responsibility_id | job_id | person_id | responsibility                                             |
|------------------:|-------:|----------:|:-----------------------------------------------------------|
|                 0 |      0 |         0 | Google stuff                                               |
|                 1 |      0 |         0 | Mark TensorFlow issues as "Won't Do"                       |
|                 2 |      1 |         0 | Censor media                                               |
|                 3 |      1 |         0 | Learn the foundations of ML                                |
|                 4 |      1 |         0 | Do Kaggle competitions                                     |
|                 5 |      2 |         1 | Assert that GPT-2 is racist                                |
|                 6 |      2 |         1 | Assert that GPT-3 is racist                                |
|                 7 |      2 |         1 | Develop a prototype of a premium non-racist language model | 
