# Glossary changes: v1.0 to v1.1

## Added Terms

### Actor
A person, organization, or system that has one or more roles that initiates or interacts with activities.

Example: The SATRE architecture needs actors such as data analysts and internal auditors.

See also: [Role].

### Application Component

An encapsulation of application functionality which is modular and replaceable.

Example: To perform work within a TRE a data analyst might need access to a Desktop or command line interface application component.

See also: [Desktop]; [Command Line Interface (CLI)].

### Architecture
An architecture defines the structures and behaviours of an organisation including people, processes, data and technology. 
This helps build a blueprint for how organisations and people work with technology to deliver TREs.

### Architectural Principle
Fundamental guidelines that inform the design, decision making and implementation of a TRE. These principles provide a 
framework to ensure that the design of the underlying components of a TRE are aligned to consistent goals, values and best practices.

See also: [Trusted Research Environment (TRE)].

### Business Process
A set of actions which produce a specific desired outcome.

Example: To access the TRE a data consumer needs to complete an onboarding business process.

See also: [User Onboarding]; [Trusted Research Environment (TRE)].

### Capability
An ability that a system possesses. Capabilities are typically expressed in general and high-level terms. 
Achieving a capability typically requires a combination of organisation, people, processes, and technology.

See also: [Capability Decomposition].

### Capability Decomposition
A set of components that realise a capability. These components will vary depending on the nature of the 
capability. Business-focused capabilities will be realised by business processes, roles and services. 
Technology-focused capabilities will be realised by applications, services and interfaces. 
In addition to the components realising the capability, a catalogue of standards, frameworks and controls 
linked to the capabilities will provide guidance on how to implement the capabilities safely.

See also: [Capability]; [Component]; [Business Process]; [Role]; [Application Component].

### Data Object
A store of data or information.

Example: To know what data is stored within the TRE a study database data object is needed. This contains information on the data assets within the TRE, who owns them and other compliance information.

See also: [Database]; [Trusted Research Environment (TRE)].

### Demilitarized Zone (DMZ)
A physical or logical subnetwork that separates an internal TRE network from untrusted external networks, such as the internet. 
The DMZ provides limited access to internal networks based on trust.

See also: [zone]

### Orchestration Zone (OZ)
The zone managing the deployment and maintenance of infrastructure and the configuration of the TRE. 
This zone contains no research data and is not be accessible to any researcher/project role. 
Infrastructure management roles operate within this zone.

See also: [zone].

### Query Management Zone (QMZ)
The zone handling queries sent to the TRE from other, remote TREs or external Job Submission services. 
Typically it sits alongside a [Research Analytics Zone (RAZ)] and provides different methods of access to 
approved research-ready datasets stored within the [Secure Data Zone (SDZ)] .

See also: [zone].

### Research Analytics Zone (RAZ)
The zone providing the means for a researcher to gain direct access to the data their project is approved to use, 
in an environment suitable for the analyses their research requires. This is often realised as a virtual desktop environment, 
a computational notebook or similar. There is often a strict requirement that project environments be completely isolated from one another.

See also: [zone].  

### Role
A role is a set of connected behaviors, rights, obligations and norms within a TRE system. Roles are occupied by individuals, who are called actors.

See also: [Actor]; [Trusted Research Environment (TRE)].

### Secure Data Zone (SDZ)
Zone supporting the management, linkage, curation and provision of research-ready sensitive datasets. Governance roles and Data Managers operate in the SDZ.

See also: [zone].

### Specification Pillar
A specification pillar is a group of related capabilities. SATRE has four specification pillars: Information governance, 
Computing technology, Data management and Supporting Capabilities.

See also: [Capability].

### Zone
A distinct area within a TRE that has specific security, access, or functional characteristics. 
Zones require different levels of governance and approval for the roles accessing them, and in particular, 
movement of data between them should be subject to appropriate controls to manage the related disclosure risks.

See also: [Orchestration Zone (OZ)].

See also: [Query Management Zone (QMZ)].

See also: [Research Analytics Zone (RAZ)].

See also: [Secure Data Zone (SDZ)].  

## Changed Definitions
### National Data Guardian
**Added to definition**: See also: [UK Government National Data Guardian](https://www.gov.uk/government/organisations/national-data-guardian/about)

### Pseudonymisation
(This was previously a placeholder.)

The replacement of direct identifiers within a dataset with pseudonyms so that the data no longer directly identifies individuals. 
In contrast to [Anonymisation], pseudonymisation provides the option of reinstating the original identifiers should they be needed and also allows for the linking of datasets through the creation of common pseudonyms.

See: [Pseudonymisation](https://www.elgaronline.com/display/book/9781035300921/b-9781035300921-P_140.xml).

See also: [Anonymisation].

See also: [Anonymisation and pseudonymisation](https://ico.org.uk/media/1061/anonymisation-code.pdf).
