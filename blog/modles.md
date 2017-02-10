In our blog
Features
========

Blog will have the following Features

1.post(Table in database)
2.Categories(Table in database)
3.Tag(Table in our database)
4.Author(Table in our database)

Let us make a relation between our tables
=========================================
1.post can have many categories, and a category can have many post(relation between Post and Category table)(ManytoMany relation)

2. a tag can have many post and a post can have many tag(ManytoMany relation)

3.author can have many post s and a post can have a single author(OneToMany relation)[ no post can write by more than authors]

Attributes for tables
=====================
Post
=====
1.title
2.created_date
3.body
4.tags
5.categories
6.Author

categories
==========
1.cat_name
2.cat_description

Author
======
1.Author name
2. Author email
3.Author bio

Tag
===
tag_name
