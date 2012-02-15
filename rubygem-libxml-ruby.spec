# Generated from libxml-ruby-2.2.2.gem by gem2rpm5 -*- rpm-spec -*-
%define	rbname	libxml-ruby

Summary:	Ruby Bindings for LibXML2
Name:		rubygem-%{rbname}

Version:	2.2.2
Release:	2
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		http://xml4r.github.com/libxml-ruby
Source0:	http://gems.rubyforge.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems 
BuildRequires:	ruby-devel
BuildRequires:	libxml2-devel

%description
The Libxml-Ruby project provides Ruby language bindings for the GNOME
Libxml2 XML toolkit. It is free software, released under the MIT License.
Libxml-ruby's primary advantage over REXML is performance - if speed
is your need, these are good libraries to consider, as demonstrated
by the informal benchmark below.

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}
BuildArch:	noarch

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q

%build
%gem_build

%install
%gem_install

%files
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/xml
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/xml/*.rb
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/libxml/*.rb
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/libxml
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec
%{ruby_sitearchdir}/*.so


%files doc
%doc %{ruby_gemdir}/doc/%{rbname}-%{version}
