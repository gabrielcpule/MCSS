## Review
- the actual code seems to be too verbose [^1]
	- the repitition of `property` and `typeof` on all elements seems so redundant
	- see ***justification*** [^5]
- Need to change the name from SCA to MCS[^2]
- Are those principles too strict? [^3]
- Could we make the `typeof` be applied automatically if any of the default classes are used?[^4] 
	- Like if `class="c-card"` is declared, it automatically adds the `typeof:"mcss:card"` 
	- See [[Ideias/Projetos/MCSS (ex-LMAOcss)(LLM css project)/Insights and notes.md#Ideas|ideas]]
- See if it's possible to change the `typeof:"mcss:component mcss:card"` to be just `typeof:"component card"`[^4]  
	- see ***Justification*** [^6]
- There is a lot on those [RFDa primer](https://www.w3.org/TR/rdfa-primer/) and [HTML + RFDa docs](https://www.w3.org/TR/html-rdfa/)
	- the rel property seems a good way to replicate properties for all elements below a tag on RFDa primer![[Pasted image 20250629150828.png]]
	- or the property copying on html + RFDA ![[Pasted image 20250629151005.png]]
- Css new functions and modules from the w3 are also really good!
	- [Css mixins](https://www.w3.org/TR/css-mixins-1/) provide a good resource for creating functions within the CSS![[Pasted image 20250629151608.png]]
	- 
## Insights
- If systems start to use this, transforming a site to a markdown would be redundant because everything on the DOM is declarative, and LLM would have a way better time making actions on a system using this CSS
- Parsing all information would be in a instant, AIs would find what they need on a instant
- This could also serve for the LLM to recreate the website using this framework, so it knows everything on a screen without needing for the site/system owner to rebuild it using the framework, it would similiar to a map for the LLM to navigate your site
- Being able to tackle accessibility for screen readers seems so good that feels almost like a scam
- if the intuit is for it to be used by a LLM, it will do most of the work filling the `property` , `content`, etc

## Ideas
- On automatically applying `typeof` based on class names: ()
> 	- This is an excellent idea for improving the developer experience and is a recommended implementation pattern for tooling built around the MCSS framework.
> 	- **Specification vs. Implementation:** The MCSS specification mandates the _final state_ of the HTML that the LLM will consume. This final artifact must contain the explicit `typeof` attribute for the reasons mentioned above.
> 	- **Tooling and Automation:** However, _how_ that attribute gets into the final HTML is an implementation detail. A build process, a PostCSS plugin, a linter with an auto-fix rule, or the rendering logic of a component framework (like React or Vue) could absolutely be designed to automatically inject `typeof="mcs:Card"` whenever it encounters `class="c-card"`. This would reduce the manual boilerplate for developers without compromising the machine-readability of the final output.
> 	- So, while the specification requires the explicit attribute in the code the AI sees, automating its insertion during development is a smart and encouraged practice.


[^1]: [[LLM-Optimized System Design Requirements_#4.3 Practical Implementation Annotating a Component]]

[^2]: [[LLM-Optimized System Design Requirements_#Section II Foundational Principles of the Semantic Component Architecture (SCA)]]

[^3]: [[LLM-Optimized System Design Requirements_#2.2 The Principle of Component Isolation and Predictable Specificity]] [[LLM-Optimized System Design Requirements_#3.3 Table The Ontological Naming Convention (ONC) Guidelines]]

[^4]: [[LLM-Optimized System Design Requirements_#Section V The SCA Annotation Schema]]

[^5]:  On the verbosity of `property` and `typeof`
	
	You are correct that the annotation layer adds verbosity to the HTML. This is an intentional design trade-off, similar to the one made by methodologies like BEM, which are also known for being verbose.[21, 22] The primary goal of MCSS is to maximize machine comprehension to achieve the 95% AI accuracy target.
	
	- **Reducing Ambiguity:** This explicit, albeit repetitive, annotation system creates a "semantic ground truth" directly within the markup. It eliminates the need for an LLM to infer a component's purpose or structure from class names alone, a process that is highly prone to error and hallucination.[23]
	- **Creating a Knowledge Graph:** The use of `property` and `typeof` transforms the HTML document into a machine-readable knowledge graph.[24, 25] This rich, structured data is far more reliable for an AI to parse than trying to reverse-engineer intent from stylistic class names. The verbosity is the cost of creating this high-fidelity data layer.
	- 

[^6]: On removing the `mcs:` prefix from `typeof`
	
	The `mcs:` prefix is a non-negotiable part of the RDFa specification and is essential for the system to work as intended.
	
	- **Disambiguation of Vocabularies:** RDFa is designed to allow the mixing of multiple, independent vocabularies on a single webpage.[26, 24] For instance, you might use the MCSS vocabulary for UI structure, the Schema.org vocabulary for product details, and the FOAF vocabulary for author information.
	- **Preventing Collisions:** The prefix is what tells a machine parser which dictionary to use for a given term. The term `Card` could exist in multiple vocabularies with different meanings (e.g., `mcs:Card` for a UI component vs. `ecommerce:Card` for a credit card). Without the `mcs:` prefix, `typeof="card"` would be ambiguous. The parser would not know which definition of "card" to apply.
	- **Semantic Web Foundation:** This use of namespaces is a core principle of the Semantic Web, ensuring that concepts can be uniquely and globally identified, which is what allows machines to process them reliably.[26, 27] Removing the prefix would break this system and defeat the purpose of using RDFa.
