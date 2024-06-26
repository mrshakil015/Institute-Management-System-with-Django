To conditionally display the search section based on the current route in a Django application:

```python
from django.urls import resolve

def contactpage(request):
    current_path = request.path
    return render(request, 'contactpage.html', {'current_path': current_path})
```

```html
<!-- header.html -->

<nav class="navbar navbar-header-left navbar-expand-lg navbar-form nav-search p-0 d-none d-lg-flex">
  {% if current_path == '/contactpage/' %}
  <div class="input-group">
    <div class="input-group-prepend">
      <button type="submit" class="btn btn-search pe-1">
        <i class="fa fa-search search-icon"></i>
      </button>
    </div>
    <input type="text" placeholder="Search ..." class="form-control" />
  </div>
  {% endif %}
</nav>

```