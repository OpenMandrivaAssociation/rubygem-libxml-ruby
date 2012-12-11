# Generated from libxml-ruby-1.1.3.gem by gem2rpm5 0.6.7 -*- rpm-spec -*-
%define	rbname	libxml-ruby

Summary:	Ruby libxml bindings
Name:		rubygem-%{rbname}

Version:	2.3.2
Release:	1
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		http://libxml.rubyforge.org/
Source0:	http://rubygems.org/downloads/%{rbname}-%{version}.gem
Patch0:		libxml-ruby-1.1.3-ruby1.9.patch
Patch1:		libxml-ruby-1.1.3-add-licenses-tag-to-metadata.patch
BuildRequires:	rubygems 
BuildRequires:	ruby-devel libxml2-devel
Provides:	rubygem-libxml
%rename		ruby-libxml

%description
The Libxml-Ruby project provides Ruby language bindings for the GNOME Libxml2
XML toolkit. It is free software, released under the MIT License.
Libxml-ruby's primary advantage over REXML is performance - if speed  is your
need, these are good libraries to consider, as demonstrated by the informal
benchmark below.

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}
BuildArch:	noarch

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q
gunzip metadata.gz
gzip metadata

%build
%gem_build

%install
%gem_install

%files
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/libxml
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/libxml/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/xml
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/xml/*.rb
%{ruby_sitearchdir}/libxml_ruby.so
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%{ruby_gemdir}/doc/%{rbname}-%{version}


%changelog
* Mon Apr 09 2012 Alexander Khrukin <akhrukin@mandriva.org> 2.3.2-1
+ Revision: 789990
- version update 2.3.2

  + Per Øyvind Karlsen <peroyvind@mandriva.org>
    - add missing licenses tag to metadata (P1)
    - fix build with ruby 1.9 (P0)
    - rename from ruby-libxml to rubygem-libxml
    - regenerate spec with gem2rpm5
    - mass rebuild of ruby packages against ruby 1.9.1

* Sun Dec 19 2010 Rémy Clouard <shikamaru@mandriva.org> 1.1.3-2mdv2011.0
+ Revision: 623176
- Fix Build
- require rubygems
- require ruby(abi) as suggested by proyvind
- Bump release
- new version 1.1.3
- use gem and %%gem_* macros to build the package
- fix URL
- fix license
- fix file list
- drop patch0 (code changed way too much in 3 years and isn?\226?\128?\153t needed
  anymore)
  TODO: remove manual untar once rpm-5.3 lands

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild
    - rebuild

* Wed Jan 02 2008 Olivier Blin <blino@mandriva.org> 0.3.4-4mdv2008.1
+ Revision: 140755
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Apr 22 2007 Pascal Terjan <pterjan@mandriva.org> 0.3.4-4mdv2008.0
+ Revision: 16811
- Use mkrel
- Use Development/Ruby group
- Use std macros

