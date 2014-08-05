#!/usr/bin/perl

=head1 NAME

index.cgi -
Print the current page of the book.

=head1 SYNOPSIS

  newpw.pl db 

=cut

######################################################################
# Modules #
###########

use CGI;        # So that we can function as a CGI script.

######################################################################
# Settings #
############

my $html;		# The HTML page returned.
my $page=0;		# The page number
my $url;		# The URL of the current page.

######################################################################
# Main #
########

my $exitval = main();
exit $exitval;

sub main {
  # Prepare to process a CGI query.
  my $query = new CGI;
  # Get the parameters
  $page = $query->param("page");
  if (!$page) { $page = 1; }
  $url = $query->self_url;
  $url =~ s/\?.*$//;
  # Set up the page number counter
  my $pagenum = 0;

  # Get the pronouns
  my @pronouns = ("he/she/ze", "she/ze/he", "ze/he/she",
                  "he/ze/she", "she/he/ze", "ze/she/he");
  my @Pronouns = ("He/She/Ze", "She/Ze/He", "Ze/He/She",
                  "He/Ze/She", "She/He/Ze", "Ze/She/He");
  my $pro = ($page % 6);
  my $pronoun = $pronouns[$pro];
  my $Pronoun = $Pronouns[$pro];

  # Get started
  print "Content-type: text/html\n\n";

  if ($page == ++$pagenum) {
    page("If You Ask Your Prof A Question",
         "",
         "<h2>A Primer on Academic Life at Grinnell</h2>"
         );
  }
  elsif ($page == ++$pagenum) {
    page("If You Ask Your Prof A Question",
         "",
         "<h2>Or ... Why Mice Don't Attend Grinnell</h2>
<h2>Or ... Why Sam Never Gets Grading Done</h2>
<h3>Samuel A. Rebelsky</h3>"
         );
  }
  elsif ($page == ++$pagenum) {
    student("If you ask your prof a question ...",
            "What is the square root of four?");
  }
  elsif ($page == ++$pagenum) {
    faculty("$Pronoun is likely to ask you a similar question.",
            "What do you think the square root of four is?");
  }
  elsif ($page == ++$pagenum) {
    student("When you answer the question,",
            "The square root of four is <em>two</em>.");
  }
  elsif ($page == ++$pagenum) {
    faculty("$Pronoun is likely to ask for an explanation.",
            "What makes you think the square root of four is two?");
  }
  elsif ($page == ++$pagenum) {
    student("When you give the explanation,",
            "My fourth grade teacher told me.");
  }
  elsif ($page == ++$pagenum) {
    faculty("$Pronoun is likely to ask for more information.",
            "I would hope that you don't trust everything your fourth-grade teacher told you.  What else leads you to believe that the square root of four is two?");
  }
  elsif ($page == ++$pagenum) {
    student("You may need to think for a little while.",
            "<em>Hmmmmmm ....</em>");
  }
  elsif ($page == ++$pagenum) {
    student("And you might even come up with an answer.",
            "Two times two is four.  So two is the square root of four.");
  }
  elsif ($page == ++$pagenum) {
    student("When you come up with an answer,",
            "<em>Whew!</em>");
  }
  elsif ($page == ++$pagenum) {
    faculty("He/Ze/She will want to make sure you've thought carefully about your answer.",
            "You said that two is <em>the</em> square root of four.  Does four, perhaps, have more than one square root?");
  }
  elsif ($page == ++$pagenum) {
    student("When you do,",
            "Okay, I know that negative two is also a square root of four.  How about <q>Two is <em>a</em> square root of four</q> or <q>two is the <em>positive</em> square root of four.");
  }
  elsif ($page == ++$pagenum) {
    faculty("$Pronoun might be impressed.",
            "See ... that wasn't so hard.");
  }
  elsif ($page == ++$pagenum) {
    faculty("However, $pronoun will also want to check the range of your understanding.",
            "You've been working in base ten.  Some ancient civilizations worked in base 60.  Computers work in base 2.  What effect does the base have on your answer?");
  }
  elsif ($page == ++$pagenum) {
    student("If you're lucky, your knowledge will be broad enough to consider the expanded question.",
            "The concept <q>two</q> is independent of the base used.  The numeral <q>2</q> in base ten is no different than the numeral <q>10</q> in base two.  Just as numeral 2 times numeral 2 base ten is equal to 4 base ten, so is numeral <q>10</q> times numeral <q>10</q> equal to <q>100</q> base two.");
  }
  elsif ($page == ++$pagenum) {
    faculty("But $pronoun will challenge you to further expand your knowledge.",
            "I'd like you to find a few references relating to your conclusion.");
  }
  elsif ($page == ++$pagenum) {
    webpage("So you'll look on the Web.",
            "<code>http://reallysimplemath.com</code>",
            "<p>As almost everyone learned in fourth grade (more or less), the square root of four is two.</p>");
  }
  elsif ($page == ++$pagenum) {
    student("You'll show your supporting evidence to your professor.",
            "It's true, I found it on the Web.");
  }
  elsif ($page == ++$pagenum) {
    faculty("$Pronoun will be impressed.",
            "The Web is crap.  Look!  The authors of this site don't even realize that four has more than one square root.");
  }
  elsif ($page == ++$pagenum) {
    faculty("But $pronoun will challenge you to find more sources.",
            "No more of this Web garbage.  Go look at something <em>printed</em>.  Print was good enough for me when I was in college, and it should be good enough for you.");
  }
  elsif ($page == ++$pagenum) {
    student("So you'll look for a textbook.",
            "Mom!  Can you send me my gradeschool books?");
  }
  elsif ($page == ++$pagenum) {
    bookpage("You might even find something.",
             "Harper &amp; Row 4th Grade Math",
             "50",
             "<p><b>Square Roots</b></p>
<p>As you may recall, the <em>square</em> of a number is the product of a number and itself.  For example, 4 is the square of 2.  We refer to the inverse of square as the <em>square root</em>.  For example, 2 is a square root of 4.  While numbers have only one square, they may have multiple square roots.  For example, negative 2 is also a square root of 4.");
  }
  elsif ($page == ++$pagenum) {
    student("When you show it to your teacher,",
            "See, my fourth grade textbook says so!");
  }
  elsif ($page == ++$pagenum) {
    faculty("$Pronoun will be impressed.",
            "It's wonderful that you can think at the level of a fourth-grade student.  I knew our standards had dropped, but I hadn't realized that they'd dropped so far.  <i>Textbooks are not appropriate sources for college students.  Elementary school textbooks are particularly inappropriate!</i>");
  }
  elsif ($page == ++$pagenum) {
    faculty("But, once again, he/she/zhe will challenge you to find more sources.",
            "Look, you're a college student.  College students look to sophisticated sources, like journal articles or scholarly texts.  Why don't you visit the library?");
  }
  elsif ($page == ++$pagenum) {
    student("You might just browse through the library",
            "<em>Hmmm ... where's the <q>really trivial math</q> section?</em>  It's Q something.  Someone told me it was on the fourth floor of Burling, but wouldn't math be in Kistle?");
  }
  elsif ($page == ++$pagenum) {
    librarian("But you're better off visiting a reference librarian.",
              "How can I help you?");
  }
  elsif ($page == ++$pagenum) {
    student("You'll tell the librarian your question.",
            "You may not believe this, but my prof wants me to find interesting journal articles and academic books on the value of the square root of four.");
  }
  elsif ($page == ++$pagenum) {
    librarian("$Pronoun will reveal a wealth of perspectives.",
              "Hmmm ....  Well, there's some recent work in the philosophy of science on the social construction of scientific knowledge.  That might help.  In computer science, there are some interesting algorithms for computing square roots.  I believe the Newton-Raphson method is a relatively simple and straightforward place to start.  Oh, group theory might also be useful, since the size of the group can affect the interpretation of multiplication.");
  }
  elsif ($page == ++$pagenum) {
    student("You'll find the sources.",
            "<em>While I love math, I hate computer science.  And I really don't even get what post-modern perspectives on the world are.  Why do I have to read this stuff?");
  }
  elsif ($page == ++$pagenum) {
    bookpage("You'll produce a bibliography.",
             "Perspectives on the Square Root of Four: An Expanded Bibliography",
             "1",
             "<p>Sokal, A. (1996). Transgressing the Boundaries: Toward a Transformative Hermeneutics of Quantum Gravity.  <i>Social Text</i> 46/47, pp. 217-252.</p>\n<p>Herstein, I. N. (1996).  <i>Abstract Algebra</i>, 3rd Edition.  John Wiley &amp; Sons.</p>\n<p>Press, W.T., Flannery, B. P., Teukolsky, S.A., and Wetterling, W. T. (1993).  <i>Numerical Recipes in C</i>.  Cambridge University Press.</p>");
  }
  elsif ($page == ++$pagenum) {
    student("And show it to your prof.",
            "Here are some <em>journal articles</em> and <em>academic texts</em>.  Are you satisfied?");
  }
  elsif ($page == ++$pagenum) {
    faculty("$Pronoun will be impressed.",
            "Three citations.  What did you do?  Just pick the first three books you saw?");
  }  
  elsif ($page == ++$pagenum) {
    faculty("In fact, $Pronoun will be so impressed by your research skills that she'll ask you to do further research.",
           "Go find at least ten <em>useful</em> sources.");
  }
  elsif ($page == ++$pagenum) {
    student("So you'll go back to the library and find more sources.",
            "");
  }
  elsif ($page == ++$pagenum) {
    bookpage("You'll revise your bibliography.",
             "Perspectives on the Square Root of Four: An <em>Expanded</em> Bibliography",
             "1",
             "<p>Sokal, A. (1996). Transgressing the Boundaries: Toward a Transformative Hermeneutics of Quantum Gravity.  <i>Social Text</i> 46/47, pp. 217-252.</p>
<p>Herstein, I. N. (1996).  <i>Abstract Algebra</i>, 3rd Edition.  John Wiley &amp; Sons.</p>
<p>Press, W.T., Flannery, B. P., Teukolsky, S.A., and Wetterling, W. T. (1993).  <i>Numerical Recipes in C</i>.  Cambridge University Press.</p>
<p>Etaoin Shrdlu (1999).  <i>Etaoin sh</i>.  Rdlu.</p>
<p>Eta, O.(2001) <i>In Shrdlu</i>.</p>
<p>...</p>");
  }
  elsif ($page == ++$pagenum) {
    student("And show it to your prof.",
            "One.  Two.  Three.  Four.  Five.  Six.  Seven.  Eight.  Nine.  Ten.  Eleven.   Eleven different sources.  Okay?");
  }
  elsif ($page == ++$pagenum) {
    faculty("$Pronoun will reflect on the purpose of bibliographies.",
            "So you can list useful books.  Did you read them?");
  }  
  elsif ($page == ++$pagenum) {
    faculty("And encourage you to read further.",
            "I want an <em>annotated</em> bibliography.");
  }  
  elsif ($page == ++$pagenum) {
    student("You'll reread the articles.",
            "<i>Post-modern reflections.  Mathematical notation.  C code.  Why me?</i>");
  }
  elsif ($page == ++$pagenum) {
    bookpage("You'll annotate your bibliography.",
             "Perspectives on the Square Root of Four: An <em>Annotated</em> Bibliography",
             "1",
             "<p>Sokal, A. (1996). Transgressing the Boundaries: Toward a Transformative Hermeneutics of Quantum Gravity.  <i>Social Text</i> 46/47, pp. 217-252.</p>
<blockquote>Sokal notes that scientific knowledge is socially constructed and applies this perspective to physical principles.</blockquote>
<p>Herstein, I. N. (1996).  <i>Abstract Algebra</i>, 3rd Edition.  John Wiley &amp; Sons.</p>
<blockquote>
A huge overview of math I cannnot hope to understand.  However, I do note that the simple groups of integers modulo various values may be useful.  In particular, 4 * 4 = 5 mod 11, so 5 is a square root of 4.
</blockquote>
<p>Press, W.T., Flannery, B. P., Teukolsky, S.A., and Wetterling, W. T. (1993).  <i>Numerical Recipes in C</i>.  Cambridge University Press.</p>
<blockquote>
We can find the square root of a number by starting at a smaller number than the square root and repeatedly trying sightly larger numbers until we find the sequare root.
</blockquote>");
  }
  elsif ($page == ++$pagenum) {
    student("And show it to your prof.",
            "See!  I can read.  Can you?");
  }
  elsif ($page == ++$pagenum) {
    bookpage("$Pronoun will observe a few small errors in your notes.",
             "Perspectives on the Square Root of Four: An <em>Annotated</em> Bibliography",
             "1",
             "<p>Sokal, A. (1996). Transgressing the Boundaries: Toward a Transformative Hermeneutics of Quantum Gravity.  <i>Social Text</i> 46/47, pp. 217-252.</p>
<blockquote>Sokal notes that scientific knowledge is socially constructed and applies this perspective to physical principles.</blockquote>
<p class=\"wrong\">Wrong!  Did you even read Sokal?</p>
<p>Herstein, I. N. (1996).  <i>Abstract Algebra</i>, 3rd Edition.  John Wiley &amp; Sons.</p>
<blockquote>
A huge overview of math I cannot hope to understand.  However, I do note that the simple groups of integers modulo various values may be useful.  In particular, 4 * 4 = 5 mod 11, so 5 is a square root of 4.
</blockquote>
<p class=\"wrong\">Wrong!  Can't you do simple math?</p>
<p>Press, W.T., Flannery, B. P., Teukolsky, S.A., and Wetterling, W. T. (1993).  <i>Numerical Recipes in C</i>.  Cambridge University Press.</p>
<blockquote>
We can find the square root of a number by starting at a smaller number than the square root and repeatedly trying sightly larger numbers until we find the sequare root.
</blockquote>
<p class=\"wrong\">While this is a method of finding very approximate square roots, it's not a very good method.  Reread the Newton-Raphson method.</p>");
  }
  elsif ($page == ++$pagenum) {
    faculty("To help you develop the skills to understand these complex readings, he/she/zhe will send you to the reading lab.",
            "It's not my job to deal with students who lack remedial skills.  Try the reading lab, but I think you're even beyond their help.");
  }
  elsif ($page == ++$pagenum) {
    student("You'll visit the reading lab.",
            "<em>Finally!  Someone here teaches me something.</em>");
  }
  elsif ($page == ++$pagenum) {
    bookpage("And update your bibliography.",
             "Perspectives on the Square Root of Four: An <em>Annotated</em> Bibliography",
             "1",
             "<p>Sokal, A. (1996). Transgressing the Boundaries: Toward a Transformative Hermeneutics of Quantum Gravity.  <i>Social Text</i> 46/47, pp. 217-252.</p>
<blockquote>In a piece of biting satire, Sokal demonstrates flaws in the post-modern view of scientific knowledge.  He concludes, implicitly, that there are some absolute scientific truths.  One such truth is that 2*2 = 4.</blockquote>
<p>Herstein, I. N. (1996).  <i>Abstract Algebra</i>, 3rd Edition.  John Wiley &amp; Sons.</p>
<blockquote>
A huge overview of math I still cannot hope to understand.  However, I do note that the simple groups of integers modulo various values may be useful.  In particular, 4 * 4 = 5 mod 11, so 4 is a square root of 5 when working in the modulus group of 11.
</blockquote>
<p>Press, W.T., Flannery, B. P., Teukolsky, S.A., and Wetterling, W. T. (1993).  <i>Numerical Recipes in C</i>.  Cambridge University Press.</p>
<blockquote>
We can find an approximation of the square root of a number by using the 
divide-and-conquer technique.  One such approach was developed by Newton
and Raphson.
</blockquote>");
  }
  elsif ($page == ++$pagenum) {
    faculty("As he/she/zhe reads your corrected annotated bibliography,",
            "Hmmm ... ");
  }
  elsif ($page == ++$pagenum) {
     faculty("A particular citation may strike your professor's eye.",
             "I see you have a book on algorithms here.  When I wrote my dissertation, I used a book on algorithms.");
  }
  elsif ($page == ++$pagenum) {
     faculty("$Pronoun will reflect on the details of the related work.",
             "Blah.  Blah.  Blah.  Blah blah.  Blah blah blah.  Blah.");
  }
  elsif ($page == ++$pagenum) {
     faculty("For two hours.",
             "Blah blah blah.  Blah.  Blah blah.  Blah.  Blah blah.  Blah blah blah.  Blah.");
  }
  elsif ($page == ++$pagenum) {
     student("When you're ready to leave,",
             "Zzzzzzzz.  Wha?  Yes, that was very interesting.");
  }
  elsif ($page == ++$pagenum) {
     faculty("$Pronoun will volunteer to loan you the reference.",
             "You'll probably find that old book an interesting contrast to your modern reference.  Let me grab it for you.  It will only take a moment.");
  }
  elsif ($page == ++$pagenum) {
     faculty("Two hours later,",
             "It's not in either file cabinet.  It's not in the two piles by my desk.  Now where is that article?");
  }
  elsif ($page == ++$pagenum) {
     faculty("$Pronoun will give up.",
             "I know I'll find it two minutes after you leave.");
  }
  elsif ($page == ++$pagenum) {
     faculty("And send you back to the library.",
             "Why don't you go look for it?  It should be easy to find.  It was an algorithms book written between 1950 and 1970.  I think it had a green cover.  Maybe blue.  The author's last name began with N.  I think the library has my thesis, so you can check the citations.  But perhaps I forgot to cite it.  Anyway, it should be easy.");
  }
  elsif ($page == ++$pagenum) {
     student("You'll return to the library",
             "Wheeeee!");  
  }
  elsif ($page == ++$pagenum) {
     librarian("And ask the friendly research librarian.",
               "Not another one of those <q>Maybe green, Maybe blue</q> requests!");
  }
  elsif ($page == ++$pagenum) {
     student("After hours of hard work,",
             "Not this one.  Not this one.  Not this one.  Not this one.  ...");
  }
  elsif ($page == ++$pagenum) {
     bookpage("You'll find the book",
              "The Blue/Green Algorithms Book",
              "42",
              "<p><i>On this page, you'll find every algorithm you'll need for your doctoral dissertation.</i></p><p>...</p>");
  }
  elsif ($page == ++$pagenum) {
     student("And bring it back to your prof.",
             "<strong>I found it!</strong>  How will it help me understand this topic?");
  }
  elsif ($page == ++$pagenum) {
     faculty("$Pronoun discuss it with you.",
             "Why did you bring that to me?  I found it two minutes after you left my office.  Anyway, I was wrong.  It's not relevant to square roots.");
  }
  elsif ($page == ++$pagenum) {
     faculty("As a reward for your hard work,",
             "Since you're here, I have to tell you I'm very impressed by the effort you've put into this topic.");
  }
  elsif ($page == ++$pagenum) {
     faculty("$Pronoun will ask you to present your results to the class.",
             "Why don't you give a presentation on it?");
  }
  elsif ($page == ++$pagenum) {
     faculty("Tomorrow.",
             "Tomorrow.");
  }
  elsif ($page == ++$pagenum) {
     student("You'll prepare it carefully.",
             "<em>Spew spew spew spew spew</em>.");
  }
  elsif ($page == ++$pagenum) {
     student("At the start of the next class,",
             "<em>I hope I'm ready.  Let's see ...  I think I'll start with <q>Today, I'd like to talk about the wonder of square roots ...</q>.");
  }
  elsif ($page == ++$pagenum) {
     faculty("$Pronoun will give you a reprieve.",
             "I don't trust you to give it today.  Why don't we go over it this afternoon first?");
  }
  elsif ($page == ++$pagenum) {
     student("When you meet to discuss it,",
             "Thanks for taking the time to go over this talk with me.  I'm quite uncomfortable about it.");
  }
  elsif ($page == ++$pagenum) {
     faculty("$Pronoun will ask you to reschedule.",
             "Did I say I'd meet with you today?  I'm booked solid with more important tasks.  Come back tomorrow.");
  }
  elsif ($page == ++$pagenum) {
     student("When you return to discuss it,",
             "Thanks for taking the time to go over this talk with me.  I'm quite uncomfortable about it.");
  }
  elsif ($page == ++$pagenum) {
     faculty("$Pronoun will ask to hear your presentation.",
             "Let's get this over with.");
  }
  elsif ($page == ++$pagenum) {
     student("After your presentation,",
             "Today, I'd like to talk about the wonder of square roots.  People from many ages and many walks of life have been stumped by the problem of computing the square root of four.  Although some aspects of square roots are socially constructed, evidence shows that the Newton-Raphson method blah blah blah blah blah.");
  }
  elsif ($page == ++$pagenum) {
     faculty("$Pronoun will give you some helpful comments.",
             "That was perhaps the worst presentation I've ever heard.");
  }
  elsif ($page == ++$pagenum) {
    faculty("And send you to the rhetoric lab.",
            "It's not my job to deal with students who lack remedial skills.  Try the rhetoric lab, but I think you're even beyond their help.");
  }
  elsif ($page == ++$pagenum) {
     student("Unfortunately,",
             "Reading lab.  Check.  Writing lab.  Check.  Library lab.  Check.  Math lab.  Check.  Science lab. Check.");
  }
  elsif ($page == ++$pagenum) {
     student("Grinnell doesn't have a rhetoric lab.",
             "I can't find it!");
  }
  elsif ($page == ++$pagenum) {
     student("So you'll return to your professor,",
             "Grinnell doesn't have a rhetoric lab.");
  }
  elsif ($page == ++$pagenum) {
     faculty("Who will volunteer to help improve your talk.",
             "Okay, I'll see what I can do.  I hate to say it, but let me hear your talk again.");
  }
  elsif ($page == ++$pagenum) {
     student("You'll give your talk again.",
             "Blah blah blah.  Newton-Raphson.  Blah blah blah. Sokal.  Blah blah blah.  Modulus.");
  }
  elsif ($page == ++$pagenum) {
     faculty("Your prof may pause for a moment ...",
             "<em>Why did we close the rhetoric and speech department?  Why did we close the rhetoric and speech department?  Why did we close the rhetoric and speech department?  And how do I convince the writing lab that they should also do presentations?</em>");
  }
  elsif ($page == ++$pagenum) {
     faculty("Before providing some helpful advice.",
             "One: Know your audience.  While I know about Sokal, modulus, and the Newton-Raphson method, your colleagues probably do not.  Explain the details.");
  }
  elsif ($page == ++$pagenum) {
     faculty("And some more.",
             "Two: Slow down.  It's not a race.");
  }
  elsif ($page == ++$pagenum) {
     faculty("And some more.",
             "Three: You don't have to tell them everything you know about the subject. Focus on the key points.");
  }
  elsif ($page == ++$pagenum) {
     faculty("And some more.",
             "Oh, don't forget to zip your fly.");
  }
  elsif ($page == ++$pagenum) {
     student("The next day,",
             "<em>I think I'm ready.  I think I'm ready.</em>");
  }
  elsif ($page == ++$pagenum) {
     student("You'll give your talk.",
             "Wisdom.  Wisdom. Wisdom. Some knowledge is absolute.  Wisdom.");
  }
  elsif ($page == ++$pagenum) {
      student("Afterward,",
              "<em>Whew!</em>");
  }
  elsif ($page == ++$pagenum) {
     faculty("$Pronoun will ask you to write a paper.",
             "That wasn't so bad.  Since you find the topic so interesting, why don't you write a ten page paper on it?");
  }
  elsif ($page == ++$pagenum) {
     faculty("For tomorrow.",
             "For tomorrow.");
  }
  elsif ($page == ++$pagenum) {
     student("You'll prepare it carefully.",
             "<em>Spew spew spew spew spew</em>.");
  }
  elsif ($page == ++$pagenum) {
     student("When you turn it in,",
             "<em>Sleep, who needs sleep?</em>");
  }
  elsif ($page == ++$pagenum) {
     faculty("$Pronoun will be so impressed that $pronoun will encourage you to write more.",
             "This looks like ten double-spaced pages.  I want ten <em>single-spaced</em> pages.");
  }
  elsif ($page == ++$pagenum) {
     faculty("For tomorrow.",
             "For tomorrow.");
  }
  elsif ($page == ++$pagenum) {
     student("When you turn it in,",
             "<em>Sleep, who needs sleep?</em>");
  }
  elsif ($page == ++$pagenum) {
     faculty("He/She/Zhe might ask you to summarize your paper.",
             "What's your thesis?");
  }
  elsif ($page == ++$pagenum) {
     student("When you do so,",
             "Two is a square root of four.");
  }
  elsif ($page == ++$pagenum) {
     faculty("$Pronoun will probably talk to you about alternatives,",
             "That's not a thesis.  Haven't you read [SimpsonE]'s guidelines for writing a thesis?");
  }
  elsif ($page == ++$pagenum) {
     faculty("Including key details.",
             "<em>1. A thesis says something a little strange.</em>  Yours doesn't.  <em>2. A thesis creates an argument that builds from one point to the next, giving the paper a direction that your reader can follow as the paper develops.</em>  Yours doesn't.  <em>3. A thesis fits comfortably into the Magic Thesis Sentence (MTS): By looking at _____, we can see _____, which most readers don't see; it is important to look at this aspect of the text because _____.</em>  Yours doesn't.  <em>4. A thesis says something about the text(s) you discuss exclusively.</em>  Yours doesn't.  <em>5. A thesis makes a lot of information irrelevant.</em>  Yours doesn't.  Try again!");
  }
  elsif ($page == ++$pagenum) {
     faculty("Afterward,",
             "What else should I suggest?");
  }
  elsif ($page == ++$pagenum) {
     faculty("$Pronoun should send you to the writing lab.",
             "Go to the writing lab.");
  }
  elsif ($page == ++$pagenum) {
    student("You'll visit the writing lab.",
            "<em>Finally!  Someone else here teaches me something.</em>");
  }
  elsif ($page == ++$pagenum) {
    bookpage("And update your thesis.",
             "Perspectives on the Square Root of Four",
             "1",
             "Although a variety of sources -- including scientific relativists, algorithmic approximators, and modular mathematicians -- have questioned the possibility of computing an exact square root, certain numbers, such as four, have exact square roots.");
  }
  elsif ($page == ++$pagenum) {
    faculty("After your prof approves the extended thesis,",
            "Well, it has about half as many words as I'd hoped for, but it's not too bad.");
  }
  elsif ($page == ++$pagenum) {
    student("You'll revise the paper.",
            "<em>Spew carefully.  Spew carefully.</em>");
  }
  elsif ($page == ++$pagenum) {
    student("When you turn in the revised version,",
            "<em>Finally!</em>");
  }
  elsif ($page == ++$pagenum) {
    faculty("Your prof may remind you about the benefits of peer review.",
            "I don't read anything that hasn't gone through at least
             two rounds of peer review.");
  }
  elsif ($page == ++$pagenum) {
    student("After you take advantage of your peer editing community,",
            "<em>Pleeeeeeeaaaasseeeee</em> read my paper!</em>");
  }
  elsif ($page == ++$pagenum) {
    faculty("Your prof may remind you about the benefits of the writing lab.",
            "I don't read anything that hasn't had careful editing by the writing lab after peer editing.");
  }
  elsif ($page == ++$pagenum) {
    student("After you get an appointment with the writing lab.",
            "Yes, I know you met with me once.  That was to work on the thesis.  Now can we work on the text itself?");
  }
  elsif ($page == ++$pagenum) {
    student("You'll probably wait a few days for your appointment.",
            "<em>Let's see ... if I lose ten percent each day it's late ...</em>");
  }
  elsif ($page == ++$pagenum) {
    student("And a few more.",
            "<em>Okay, next time I make the appointment a month in advance.</em>");
  }
  elsif ($page == ++$pagenum) {
    student("After you meet with the writing lab,",
            "<em>Oooh.  I hadn't thought about that.  Good idea!</em>");
  }
  elsif ($page == ++$pagenum) {
    student("You might take the time to incorporate their suggestions.",
            "It's already five days late.  Oh well, I might as well spend one more day on it.");
  }
  elsif ($page == ++$pagenum) {
    student("When you turn it in,",
            "I know this is late, but ...");
  }
  elsif ($page == ++$pagenum) {
    faculty("Your prof will remind you of other key writing habits.",
            "There should be two spaces after each period.  You used only one.  I refuse to grade this.");
  }
  elsif ($page == ++$pagenum) {
    student("So you'll fix it.",
            "<em>Edit.  Edit.  Edit.  Edit.</em>");
  }
  elsif ($page == ++$pagenum) {
    student("And fix it.",
            "<em>Edit.  Edit.  Edit.  Edit.</em>");
  }
  elsif ($page == ++$pagenum) {
    student("And fix it.",
            "<em>Edit.  Edit.  Edit.  Edit.</em>");
  }
  elsif ($page == ++$pagenum) {
    student("And turn it in.",
            "<em>Sleep.  Who needs sleep?</em>");
  }
  elsif ($page == ++$pagenum) {
    student("When you get it back,",
            "<em>Didn't I write a paper for this class a few weeks ago?</em>");
  }
  elsif ($page == ++$pagenum) {
     faculty("You might be pleasantly surprised.",
             "Your paper was very nice, much nicer than I expected.  I've waived the late penalty.");
  }
  elsif ($page == ++$pagenum) {
     faculty("Your faculty member might be so impressed,",
             "Your paper has inspired me.");
  }
  elsif ($page == ++$pagenum) {
     webpage("That $pronoun creates a conference.",
             "http://www.grinnell.edu/academic/general/events/conferences/faculty-sponsored/square-roots/",
             "<p><strong>Square Roots: A Post-Technological Perspective</strong></p>  <p><em>Day One: Absolute Knowledge and the Social Construction of Social Constructivism.</em></p>  <p><em>Day Two: Group Theory and the Theory of Groups.</em></p>  <p><em>Day Three: Archaeology of Ancient Algorithms.</em></p>");
  }
  elsif ($page == ++$pagenum) {
     student("After the conference,",
             "<em>Three days of talks!  Ouch.</em>");
  }
  elsif ($page == ++$pagenum) {
     faculty("$Pronoun might quiz the class about the conference.",
             "Compare and contrast social constructivism, group theory, and asymptotic analysis.  You have ten minutes.");
  }
  elsif ($page == ++$pagenum) {
     faculty("After the quiz,", "Time!");
  }
  elsif ($page == ++$pagenum) {
     student("$Pronoun might notice some puzzled faces.", "<em>Wha?</em>");
  }
  elsif ($page == ++$pagenum) {
     faculty("And when a prof notices puzzled faces,",
             "Some of you seem a little puzzled.");
  }
  elsif ($page == ++$pagenum) {
     faculty("$Pronoun will probably ask for questions.",
             "<strong>Any questions?</strong>");
  }
  elsif ($page == ++$pagenum) {
    page("A Moral", "", "<h2>Ask the right questions.</h2>");
  }
  elsif ($page == ++$pagenum) {
    page("A Moral", "", "<h2>Take advantage of Grinnell's resources.</h2>");
  }
  elsif ($page == ++$pagenum) {
    page("A Moral", "", "<h2>Laugh at your stress.</h2>");
  }
  else {
    $page = 0;
    page("The End", "", "");
  }
  # That's it, we're done.
  return 0;
} # main

# faculty(caption,quote)
sub faculty{
  my $caption = shift;
  my $quote = shift;
  my $body =<<"FACULTY";
<h1 class="caption">$caption</h1>
<table width="100%">
<tr valign="top">
<td class="left" width="50%" align="right"><img src="faculty.jpg" alt="a picture of a faculty member"></td>
<td class="right"><p class="faculty">$quote</p></td>
</tr>
</table>
FACULTY
  page("Page " . $page, $caption, $body);
}   

# librarian(caption,quote)
sub librarian {
  my $caption = shift;
  my $quote = shift;
  my $body =<<"LIBRARIAN";
<h1 class="caption">$caption</h1>
<table width="100%">
<tr valign="top">
<td class="left" width="50%" align="right"><img src="librarian.jpg" width="100pt" alt="a picture of a faculty member"></td>
<td class="right"><p class="librarian">$quote</p></td>
</tr>
</table>
LIBRARIAN
  page("Page " . $page, $caption, $body);
}   

# bookpage(caption,title,page,pagetext)
sub bookpage {
  my $caption = shift;
  my $title = shift;
  my $num = shift;
  my $pagetext = shift;
  my $body =<<"BOOKPAGE";
<h1 class="caption">$caption</h1>
<div class="webpage">
<p class="booktitle">$title</p>
$pagetext
<p class="bookpage">$num</p>
</div>
BOOKPAGE
  page("Page " . $page, $caption, $body);
}   

# webpage(caption,url,pagetext)
sub webpage {
  my $caption = shift;
  my $url = shift;
  my $pagetext = shift;
  my $body =<<"WEBPAGE";
<h1 class="caption">$caption</h1>
<div class="webpage">
<p><code>$url</code></p>
$pagetext
</div>
WEBPAGE
  page("Page " . $page, $caption, $body);
}   

# student(caption,quote)
sub student {
  my $caption = shift;
  my $quote = shift;
  my $body =<<"STUDENT";
<h1 class="caption">$caption</h1>
<table width="100%">
<tr valign="top">
<td class="left" width="50%"><p class="student" alt="a picture of a student">$quote</p></td>
<td class="right"><img src="student.jpg"></td>
</tr>
</table>
STUDENT
  page("Page " . $page, $caption, $body);
}   

# page(title,caption,body)
sub page {
  my $title = shift;
  my $caption = shift;
  my $body = shift;
  # Set up the level-1 heading.  There's no such heading if
  # there's text for the story.
  my $h1 = "";  
  if (!$caption) { $h1 = "<h1>$title</h1>"; }
  # Set up the navigation bar
  # my $nav = "<p class=\"nav\">[<a href=\"$url?page=1\">Start</a>]\n";
  my $nav = "<p class=\"nav\">\n";
  my $prevpage = $page - 1;
  my $nextpage = $page + 1;
  if ($page > 1) {
    $nav .= "<a href=\"$url?page=$prevpage\">&lt; Prev</a>\n";
  }
  if ($page) {
    $nav .= "<b>Page $page</b>\n<a href=\"$url?page=$nextpage\">Next &gt;</a>\n";
  }
  $nav .= "<\/p>\n";
  my $html =<<"PAGE";
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"
   "http://www.w3.org/TR/html4/strict.dtd">
<html lang="en">
<head>
<META http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>$title</title>
<link rel="stylesheet" type="text/css" href="askprof.css">
<script language="javascript">
document.onkeypress = function(evt) {
  // Get the code for the character using one of the many alternatives
  var code = evt.which || evt.keyCode || evt.charCode;
  switch (code) {
    case 32: // Space bar
      document.location = "?page=$nextpage";
      break;
  } // switch 
}; // document.onkeypress
</script>
</head>
<body>
<div class="bookpage">
<p class="title"><a href="?page=1">If You Ask Your Prof a Question</a></p>
$nav
$h1
$body
</div>
<p class="endnotes">This is <em>draft</em> 0.1.2 of a work in progress by
Samuel A. Rebelsky.  It is Copyright &copy; 2003-14 by Samuel A. Rebelsky.
All rights reserved.  Images are taken from the Grinnell Web Site and 
used without permission.</p>
</body>
</html>
PAGE
  print $html;
} # page


# pronoun(page)
# Pronoun(page)
#   Generate the next pronoun set
sub pronoun() {
  my $page = shift;
  return $page . $lcPronouns[$page % 6];
} # pronoun
sub Pronoun($page) {
  my $page = shift;
  return $page . $lcPronouns[$page % 6];
} # Pronoun
