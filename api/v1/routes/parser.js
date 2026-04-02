const fs = require('fs');
const path = require('path');

class Parser {
  constructor(options = {}) {
    this.options = {
      encoding: 'utf8',
      ...options,
    };
  }

  async parseFile(filePath) {
    try {
      const absolutePath = path.resolve(filePath);
      const fileContent = await fs.promises.readFile(absolutePath, this.options.encoding);
      return this._parseContent(fileContent);
    } catch (error) {
      throw new Error(`Failed to parse file: ${error.message}`);
    }
  }

  _parseContent(content) {
    try {
      return JSON.parse(content);
    } catch (error) {
      throw new Error(`Invalid JSON content: ${error.message}`);
    }
  }

  static validateSchema(data, schema) {
    if (!data || typeof data !== 'object') {
      throw new Error('Data must be a valid object');
    }

    const missingFields = [];
    for (const key in schema) {
      if (!data.hasOwnProperty(key)) {
        missingFields.push(key);
      }
    }

    if (missingFields.length > 0) {
      throw new Error(`Missing required fields: ${missingFields.join(', ')}`);
    }

    return true;
  }
}

module.exports = Parser;