Name:		texlive-njustthesis
Version:	62451
Release:	2
Summary:	Thesis template for the Nanjing University of Science and Technology
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/njustthesis
License:	gpl3+
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/njustthesis.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/njustthesis.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/njustthesis.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a thesis template for the Nanjing University of Science
and Technology>.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/njustthesis
%{_texmfdistdir}/tex/latex/njustthesis
%doc %{_texmfdistdir}/doc/latex/njustthesis

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
