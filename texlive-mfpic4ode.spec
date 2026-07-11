%global tl_name mfpic4ode
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.4
Release:	%{tl_revision}.1
Summary:	Macros to draw direction fields and solutions of ODEs
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/mfpic4ode
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mfpic4ode.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mfpic4ode.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mfpic4ode.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package is a small set of macros for drawing direction fields, phase
portraits and trajectories of differential equations and two dimensional
autonomous systems. The Euler, Runge-Kutta and 4th order Runge-Kutta
algorithms are available to solve the ODEs. The picture is translated
into mfpic macros and MetaPost is used to create the final drawing. The
package is was designed for use with LaTeX, but it can be used in plain
TeX as well.

