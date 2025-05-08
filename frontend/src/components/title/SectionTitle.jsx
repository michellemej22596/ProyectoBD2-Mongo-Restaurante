import "./sectionTitle.css"

const SectionTitle = ({ subtitle, title}) => {
    return (
        <div>
            <span className='section-subtitle'>{subtitle}</span>
            <h2 className='section-title'>{title}</h2>
        </div>
    )
}
export default SectionTitle