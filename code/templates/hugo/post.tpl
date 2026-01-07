---
title: {{ post.title.rendered.replace(":", "-") }}
date: {{ post.date.replace("T", " ") }}
tags:
    {% for i in post.category %}
    - {{ i }}
    {% if not loop.last %}{% endif %}
    {% endfor %} 
categories:
    {% for i in post.category %}
    - {{ i }}
    {% if not loop.last %}{% endif %}
    {% endfor %} 
keywords: 
    {% for i in post.category %}
    - {{ i }}
    {% if not loop.last %}{% endif %}
    {% endfor %} 
---
{{ post.content.rendered }}