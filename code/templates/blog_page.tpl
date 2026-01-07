<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="utf-8">
    <link rel="icon" href="img/favicon.ico" type="image/png">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="Spent most of my days with a shell, deploys apps, writing code ore fixing problems with automating, This is some of the stuff a work on right now " />
        <meta name="keywords" content="kubernernetes samma.io sre linux docker devops ks8 help blog fix problems" />
        <meta property="og:title" content="Lifeandshell - Mattias Hemmingsson" />
        <meta property="og:type" content="devsecops devops sre drones hacking" />
        <meta property="og:url" content="https://lifeadnshell.com" />
        <meta property="og:description" content="Lifeandshell - Mattias Hemmingsson - SRE Devops - And more " />

    <title>Mattias Hemmingsson</title>
    <!-- font icons -->
    <link rel="stylesheet" href="/assets/vendors/themify-icons/css/themify-icons.css">
    <!-- Bootstrap + Steller main styles -->
	<link rel="stylesheet" href="/assets/css/steller.css">

    <!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-3SYH00HY9X"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-3SYH00HY9X');
</script>
</head>
<body data-spy="scroll" data-target=".navbar" data-offset="40" id="home">

    <!-- Page navigation -->
    <nav class="navbar navbar-expand-lg navbar-light fixed-top" data-spy="affix" data-offset-top="0">
        <div class="container">
            <a class="navbar-brand" href="#"><img src="/img/hrb.png" alt=""></a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>

            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav ml-auto align-items-center">
                    <li class="nav-item">
                        <a class="nav-link" href="/">Home</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="/blog">Blog</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="/">Contact</a>
                    </li>
                </ul>
            </div>
        </div>          
    </nav>
    <!-- End of page navibation -->


    <!-- Blog Section -->
    <section id="blog" class="section">
        <div class="container text-center">
            <h6 class="subtitle">My Blogs</h6>
            <p class="mb-5 pb-4"></p>

            <div class="row text-left">
{% for post in posts -%}

            
                <div class="col-md-4">
                    <div class="card border mb-4">
                        <img src="assets/imgs/blog-1.jpg" alt="" class="card-img-top w-100">
                        <div class="card-body">

                            <h5 class="card-title">{{ post.title.rendered }}</h5>
                            <div class="post-details">
                                <a href="javascript:void(0)">{{ post.date }}</a>
                            </div>
                            <p></p>
                            <a href="/blog/{{ post.slug}}/">Read More..</a>
                        </div>
                    </div>
                </div>
                {% endfor %}

            </div>
        </div>
    </section>

            


    <!-- Page Footer -->
    <footer class="page-footer">
        <div class="container">
            <div class="row align-items-center">
                <div class="col-sm-6">
                    <p>Copyright <script>document.write(new Date().getFullYear())</script> &copy; <a href="http://hacking.robots.beer" target="_blank">Mattias Hemmingsson / h.r.b AB </a></p>
                </div>
                <div class="col-sm-6">
                    <div class="socials">
                        <a class="social-item" href="javascript:void(0)"><i class="ti-github"></i></a>
                    </div>
                </div>
            </div>
        </div>
    </footer> 
    <!-- End of page footer -->
	
	<!-- core  -->
    <script src="/assets/vendors/jquery/jquery-3.4.1.js"></script>
    <script src="/assets/vendors/bootstrap/bootstrap.bundle.js"></script>
    <!-- bootstrap 3 affix -->
	<script src="/assets/vendors/bootstrap/bootstrap.affix.js"></script>

    <!-- steller js -->
    <script src="/assets/js/steller.js"></script>

</body>
</html>
