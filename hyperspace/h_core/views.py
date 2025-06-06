from datetime import datetime
from django.shortcuts import render
from services.models import Services

def index(request):
    static_context="""
<section id="intro" class="wrapper style1 fullscreen fade-up">
						<div class="inner">
							<h1>Hyperspace</h1>
							
							<p>Just another fine responsive site template designed by <a href="http://html5up.net">HTML5 UP</a><br />
							and released for free under the <a href="http://html5up.net/license">Creative Commons</a>.</p>
							<ul class="actions">
								<li><a href="#one" class="button scrolly">Learn more</a></li>
							</ul>
						</div>
					</section>
    """
    featured_services=Services.objects.filter(IsFeatured=True)
    
    context={
       'static_context': static_context,
       'featured_services':featured_services,
    }
    return render (request, 'h_core/index.html',context)