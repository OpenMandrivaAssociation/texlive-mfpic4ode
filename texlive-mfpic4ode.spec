Name:		texlive-mfpic4ode
Version:	17745
Release:	2
Summary:	Macros to draw direction fields and solutions of ODEs
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/mfpic4ode
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mfpic4ode.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mfpic4ode.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mfpic4ode.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package is a small set of macros for drawing direction
fields, phase portraits and trajectories of differential
equations and two dimensional autonomous systems. The Euler,
Runge-Kutta and 4th order Runge-Kutta algorithms are available
to solve the ODEs. The picture is translated into mfpic macros
and MetaPost is used to create the final drawing. The package
is was designed for use with LaTeX, but it can be used in plain
TeX as well. Online demonstration of the mfpic4ode macros is
available on the Mfpic Previewer as Example 6.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/mfpic4ode/mfpic4ode.sty
%{_texmfdistdir}/tex/latex/mfpic4ode/mfpic4ode.tex
%doc %{_texmfdistdir}/doc/latex/mfpic4ode/README
%doc %{_texmfdistdir}/doc/latex/mfpic4ode/demo/demo-plain.pdf
%doc %{_texmfdistdir}/doc/latex/mfpic4ode/demo/demo-plain.tex
%doc %{_texmfdistdir}/doc/latex/mfpic4ode/demo/demo.pdf
%doc %{_texmfdistdir}/doc/latex/mfpic4ode/demo/demo.tex
%doc %{_texmfdistdir}/doc/latex/mfpic4ode/mfpic4ode.pdf
#- source
%doc %{_texmfdistdir}/source/latex/mfpic4ode/mfpic4ode.dtx
%doc %{_texmfdistdir}/source/latex/mfpic4ode/mfpic4ode.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
